# Generated from ConfigLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ConfigLangParser import ConfigLangParser
else:
    from ConfigLangParser import ConfigLangParser

# This class defines a complete listener for a parse tree produced by ConfigLangParser.
class ConfigLangListener(ParseTreeListener):

    # Enter a parse tree produced by ConfigLangParser#config.
    def enterConfig(self, ctx:ConfigLangParser.ConfigContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#config.
    def exitConfig(self, ctx:ConfigLangParser.ConfigContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#statement.
    def enterStatement(self, ctx:ConfigLangParser.StatementContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#statement.
    def exitStatement(self, ctx:ConfigLangParser.StatementContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:ConfigLangParser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:ConfigLangParser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#value.
    def enterValue(self, ctx:ConfigLangParser.ValueContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#value.
    def exitValue(self, ctx:ConfigLangParser.ValueContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#dictionary.
    def enterDictionary(self, ctx:ConfigLangParser.DictionaryContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#dictionary.
    def exitDictionary(self, ctx:ConfigLangParser.DictionaryContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#pair.
    def enterPair(self, ctx:ConfigLangParser.PairContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#pair.
    def exitPair(self, ctx:ConfigLangParser.PairContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#array.
    def enterArray(self, ctx:ConfigLangParser.ArrayContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#array.
    def exitArray(self, ctx:ConfigLangParser.ArrayContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#constantExpression.
    def enterConstantExpression(self, ctx:ConfigLangParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#constantExpression.
    def exitConstantExpression(self, ctx:ConfigLangParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#expression.
    def enterExpression(self, ctx:ConfigLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#expression.
    def exitExpression(self, ctx:ConfigLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#sum.
    def enterSum(self, ctx:ConfigLangParser.SumContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#sum.
    def exitSum(self, ctx:ConfigLangParser.SumContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#product.
    def enterProduct(self, ctx:ConfigLangParser.ProductContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#product.
    def exitProduct(self, ctx:ConfigLangParser.ProductContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#atom.
    def enterAtom(self, ctx:ConfigLangParser.AtomContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#atom.
    def exitAtom(self, ctx:ConfigLangParser.AtomContext):
        pass


    # Enter a parse tree produced by ConfigLangParser#functionCall.
    def enterFunctionCall(self, ctx:ConfigLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ConfigLangParser#functionCall.
    def exitFunctionCall(self, ctx:ConfigLangParser.FunctionCallContext):
        pass



del ConfigLangParser