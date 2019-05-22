# Generated from Grammar.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from generated.GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#eof.
    def visitEof(self, ctx:GrammarParser.EofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#gl.
    def visitGl(self, ctx:GrammarParser.GlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#main.
    def visitMain(self, ctx:GrammarParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#line.
    def visitLine(self, ctx:GrammarParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ifst.
    def visitIfst(self, ctx:GrammarParser.IfstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#boolex.
    def visitBoolex(self, ctx:GrammarParser.BoolexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arg.
    def visitArg(self, ctx:GrammarParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#simple_variable_operation.
    def visitSimple_variable_operation(self, ctx:GrammarParser.Simple_variable_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#op_application.
    def visitOp_application(self, ctx:GrammarParser.Op_applicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forst.
    def visitForst(self, ctx:GrammarParser.ForstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#strr.
    def visitStrr(self, ctx:GrammarParser.StrrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variables.
    def visitVariables(self, ctx:GrammarParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable.
    def visitVariable(self, ctx:GrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expansion.
    def visitExpansion(self, ctx:GrammarParser.ExpansionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#cin.
    def visitCin(self, ctx:GrammarParser.CinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#cout.
    def visitCout(self, ctx:GrammarParser.CoutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#retst.
    def visitRetst(self, ctx:GrammarParser.RetstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variablename.
    def visitVariablename(self, ctx:GrammarParser.VariablenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#typename.
    def visitTypename(self, ctx:GrammarParser.TypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#strexp.
    def visitStrexp(self, ctx:GrammarParser.StrexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#numeric.
    def visitNumeric(self, ctx:GrammarParser.NumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#semicolon.
    def visitSemicolon(self, ctx:GrammarParser.SemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignment.
    def visitAssignment(self, ctx:GrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arithmetic.
    def visitArithmetic(self, ctx:GrammarParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#star.
    def visitStar(self, ctx:GrammarParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#homer.
    def visitHomer(self, ctx:GrammarParser.HomerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#comma.
    def visitComma(self, ctx:GrammarParser.CommaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#unary.
    def visitUnary(self, ctx:GrammarParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#lbra.
    def visitLbra(self, ctx:GrammarParser.LbraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rbra.
    def visitRbra(self, ctx:GrammarParser.RbraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#lpar.
    def visitLpar(self, ctx:GrammarParser.LparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rpar.
    def visitRpar(self, ctx:GrammarParser.RparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#lsq.
    def visitLsq(self, ctx:GrammarParser.LsqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rsq.
    def visitRsq(self, ctx:GrammarParser.RsqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#logic.
    def visitLogic(self, ctx:GrammarParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#leftarrows.
    def visitLeftarrows(self, ctx:GrammarParser.LeftarrowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rightarrows.
    def visitRightarrows(self, ctx:GrammarParser.RightarrowsContext):
        return self.visitChildren(ctx)



del GrammarParser