import sys
sys.path.append('.')
import json
from antlr4 import *
from ConfigLangLexer import ConfigLangLexer
from ConfigLangParser import ConfigLangParser
from ConfigLangVisitor import ConfigLangVisitor
from antlr4.error.ErrorListener import ErrorListener

class ConfigLangEvaluator(ConfigLangVisitor):
    """
    Обходчик AST для вычисления констант и преобразования в Python-объекты.
    """
    def __init__(self):
        self.constants = {}

    # --- Главные правила ---

    def visitConfig(self, ctx: ConfigLangParser.ConfigContext):
        """Обрабатывает корневой узел и возвращает список элементов конфигурации."""
        result = []
        for statement in ctx.statement():
            val = self.visit(statement)
            if val is not None:
                result.append(val)
        return result

    def visitStatement(self, ctx: ConfigLangParser.StatementContext):
        """Обрабатывает объявление константы или значение."""
        if ctx.constantDeclaration():
            return self.visit(ctx.constantDeclaration())
        elif ctx.value():
            return self.visit(ctx.value())
        return None

    # --- Объявление константы ---

    def visitConstantDeclaration(self, ctx: ConfigLangParser.ConstantDeclarationContext):
        """Обрабатывает объявление константы и сохраняет ее значение."""
        name = ctx.NAME().getText()
        value = self.visit(ctx.value())
        self.constants[name] = value
        return None # Объявления констант не попадают в финальный JSON

    # --- Структуры данных ---

    def visitValue(self, ctx: ConfigLangParser.ValueContext):
        """Обрабатывает значение."""
        if ctx.dictionary():
            return self.visit(ctx.dictionary())
        elif ctx.array():
            return self.visit(ctx.array())
        elif ctx.NUMBER():
            return self.visit(ctx.NUMBER())
        elif ctx.constantExpression():
            return self.visit(ctx.constantExpression())
        return None

    def visitDictionary(self, ctx: ConfigLangParser.DictionaryContext):
        """Преобразует словарь в Python dict."""
        d = {}
        for pair in ctx.pair():
            key, value = self.visit(pair)
            d[key] = value
        return d

    def visitPair(self, ctx: ConfigLangParser.PairContext):
        """Преобразует пару ключ-значение."""
        key = ctx.NAME().getText()
        value = self.visit(ctx.value())
        return (key, value)

    def visitArray(self, ctx: ConfigLangParser.ArrayContext):
        """Преобразует массив в Python list."""
        arr = []
        for value in ctx.value():
            arr.append(self.visit(value))
        return arr

    # --- Вычисление константных выражений ---

    def visitConstantExpression(self, ctx: ConfigLangParser.ConstantExpressionContext):
        """Вычисляет константное выражение."""
        return self.visit(ctx.expression())

    def visitSum(self, ctx: ConfigLangParser.SumContext):
        """Вычисляет сумму и разность."""
        result = self.visit(ctx.product(0))
        for i in range(1, len(ctx.product())):
            op = ctx.getChild(2 * i - 1).getText()
            value = self.visit(ctx.product(i))
            if op == '+':
                result += value
            elif op == '-':
                result -= value
        return result

    def visitProduct(self, ctx: ConfigLangParser.ProductContext):
        """Обрабатывает product (который в нашей грамматике - это atom)."""
        return self.visit(ctx.atom())

    def visitAtom(self, ctx: ConfigLangParser.AtomContext):
        """Обрабатывает атомарные элементы выражения."""
        if ctx.NAME():
            name = ctx.NAME().getText()
            if name not in self.constants:
                raise ValueError(f"Необъявленная константа: {name}")
            return self.constants[name]
        elif ctx.NUMBER():
            return self.visit(ctx.NUMBER())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.LPAREN(): # Вложенное выражение в скобках
            # sum - это единственный нетерминальный дочерний элемент между скобками
            # В ANTLR, если правило имеет альтернативы, то контекст родителя
            # может не иметь прямого метода для дочернего правила, если оно
            # не является частью именованной альтернативы.
            # В данном случае, sum() должен быть доступен.
            # Если нет, то нужно использовать getChild(1) для получения sumContext.
            # Но, согласно грамматике, sum() должен быть.
            # Попробуем использовать getChild(1) для получения sumContext.
            # ctx.getChild(1) - это sumContext
            return self.visit(ctx.getChild(1))
        return None

    def visitFunctionCall(self, ctx: ConfigLangParser.FunctionCallContext):
        """Обрабатывает вызов функции len()."""
        func_name = ctx.LEN().getText()
        # Аргумент может быть NAME, array, или dictionary.
        if ctx.NAME():
            name = ctx.NAME().getText()
            if name not in self.constants:
                raise ValueError(f"Необъявленная константа: {name}")
            arg = self.constants[name]
        elif ctx.array():
            arg = self.visit(ctx.array())
        elif ctx.dictionary():
            arg = self.visit(ctx.dictionary())
        else:
            # Это должно быть невозможно, если грамматика корректна
            raise ValueError("Некорректный аргумент для len()")

        if func_name == 'len':
            if isinstance(arg, (list, dict)):
                return float(len(arg))
            else:
                raise ValueError(f"len() не применима к типу {type(arg)}")
        else:
            raise NotImplementedError(f"Неизвестная функция: {func_name}")

    # --- Токены ---

    def visitTerminal(self, node):
        """Обрабатывает терминальные узлы (токены)."""
        if node.symbol.type == ConfigLangLexer.NUMBER:
            return float(node.getText())
        return super().visitTerminal(node)

class CustomErrorListener(ErrorListener):
    """Кастомный слушатель ошибок для обработки синтаксических ошибок."""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Синтаксическая ошибка в строке {line}, столбце {column}: {msg}")

def main():
    """Основная функция инструмента командной строки."""
    try:
        # 1. Чтение входного текста из стандартного ввода
        config_text = sys.stdin.read()
        
        # 2. Инициализация лексера и парсера
        input_stream = InputStream(config_text)
        lexer = ConfigLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ConfigLangParser(stream)
        
        # Установка кастомного слушателя ошибок
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())
        
        # 3. Парсинг
        tree = parser.config()
        
        # 4. Обход AST, вычисление констант и преобразование
        evaluator = ConfigLangEvaluator()
        result = evaluator.visit(tree)
        
        # 5. Вывод результата в формате JSON в стандартный вывод
        # Если в результате только один элемент, выводим его напрямую, иначе - список.
        if len(result) == 1 and isinstance(result[0], (dict, list, float)):
            json_output = json.dumps(result[0], indent=4)
        else:
            json_output = json.dumps(result, indent=4)
            
        sys.stdout.write(json_output + "\n")

    except SyntaxError as e:
        sys.stderr.write(f"Синтаксическая ошибка: {e}\n")
        sys.exit(1)
    except ValueError as e:
        sys.stderr.write(f"Ошибка вычисления константы: {e}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Непредвиденная ошибка: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
