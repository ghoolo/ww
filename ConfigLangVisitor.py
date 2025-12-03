# Generated from ConfigLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ConfigLangParser import ConfigLangParser
else:
    from ConfigLangParser import ConfigLangParser

# This class defines a complete generic visitor for a parse tree produced by ConfigLangParser.

class ConfigLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConfigLangParser#config.
    def visitConfig(self, ctx:ConfigLangParser.ConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#statement.
    def visitStatement(self, ctx:ConfigLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:ConfigLangParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#value.
    def visitValue(self, ctx:ConfigLangParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#dictionary.
    def visitDictionary(self, ctx:ConfigLangParser.DictionaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#pair.
    def visitPair(self, ctx:ConfigLangParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#array.
    def visitArray(self, ctx:ConfigLangParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#constantExpression.
    def visitConstantExpression(self, ctx:ConfigLangParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#expression.
    def visitExpression(self, ctx:ConfigLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#sum.
    def visitSum(self, ctx:ConfigLangParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#product.
    def visitProduct(self, ctx:ConfigLangParser.ProductContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#atom.
    def visitAtom(self, ctx:ConfigLangParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConfigLangParser#functionCall.
    def visitFunctionCall(self, ctx:ConfigLangParser.FunctionCallContext):
        return self.visitChildren(ctx)



del ConfigLangParser