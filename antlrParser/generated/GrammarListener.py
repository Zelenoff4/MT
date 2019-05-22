# Generated from Grammar.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from generated.GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#eof.
    def enterEof(self, ctx:GrammarParser.EofContext):
        pass

    # Exit a parse tree produced by GrammarParser#eof.
    def exitEof(self, ctx:GrammarParser.EofContext):
        pass


    # Enter a parse tree produced by GrammarParser#gl.
    def enterGl(self, ctx:GrammarParser.GlContext):
        pass

    # Exit a parse tree produced by GrammarParser#gl.
    def exitGl(self, ctx:GrammarParser.GlContext):
        pass


    # Enter a parse tree produced by GrammarParser#main.
    def enterMain(self, ctx:GrammarParser.MainContext):
        pass

    # Exit a parse tree produced by GrammarParser#main.
    def exitMain(self, ctx:GrammarParser.MainContext):
        pass


    # Enter a parse tree produced by GrammarParser#line.
    def enterLine(self, ctx:GrammarParser.LineContext):
        pass

    # Exit a parse tree produced by GrammarParser#line.
    def exitLine(self, ctx:GrammarParser.LineContext):
        pass


    # Enter a parse tree produced by GrammarParser#ifst.
    def enterIfst(self, ctx:GrammarParser.IfstContext):
        pass

    # Exit a parse tree produced by GrammarParser#ifst.
    def exitIfst(self, ctx:GrammarParser.IfstContext):
        pass


    # Enter a parse tree produced by GrammarParser#boolex.
    def enterBoolex(self, ctx:GrammarParser.BoolexContext):
        pass

    # Exit a parse tree produced by GrammarParser#boolex.
    def exitBoolex(self, ctx:GrammarParser.BoolexContext):
        pass


    # Enter a parse tree produced by GrammarParser#arg.
    def enterArg(self, ctx:GrammarParser.ArgContext):
        pass

    # Exit a parse tree produced by GrammarParser#arg.
    def exitArg(self, ctx:GrammarParser.ArgContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#simple_variable_operation.
    def enterSimple_variable_operation(self, ctx:GrammarParser.Simple_variable_operationContext):
        pass

    # Exit a parse tree produced by GrammarParser#simple_variable_operation.
    def exitSimple_variable_operation(self, ctx:GrammarParser.Simple_variable_operationContext):
        pass


    # Enter a parse tree produced by GrammarParser#op_application.
    def enterOp_application(self, ctx:GrammarParser.Op_applicationContext):
        pass

    # Exit a parse tree produced by GrammarParser#op_application.
    def exitOp_application(self, ctx:GrammarParser.Op_applicationContext):
        pass


    # Enter a parse tree produced by GrammarParser#forst.
    def enterForst(self, ctx:GrammarParser.ForstContext):
        pass

    # Exit a parse tree produced by GrammarParser#forst.
    def exitForst(self, ctx:GrammarParser.ForstContext):
        pass


    # Enter a parse tree produced by GrammarParser#strr.
    def enterStrr(self, ctx:GrammarParser.StrrContext):
        pass

    # Exit a parse tree produced by GrammarParser#strr.
    def exitStrr(self, ctx:GrammarParser.StrrContext):
        pass


    # Enter a parse tree produced by GrammarParser#variables.
    def enterVariables(self, ctx:GrammarParser.VariablesContext):
        pass

    # Exit a parse tree produced by GrammarParser#variables.
    def exitVariables(self, ctx:GrammarParser.VariablesContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable.
    def enterVariable(self, ctx:GrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable.
    def exitVariable(self, ctx:GrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by GrammarParser#expansion.
    def enterExpansion(self, ctx:GrammarParser.ExpansionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expansion.
    def exitExpansion(self, ctx:GrammarParser.ExpansionContext):
        pass


    # Enter a parse tree produced by GrammarParser#cin.
    def enterCin(self, ctx:GrammarParser.CinContext):
        pass

    # Exit a parse tree produced by GrammarParser#cin.
    def exitCin(self, ctx:GrammarParser.CinContext):
        pass


    # Enter a parse tree produced by GrammarParser#cout.
    def enterCout(self, ctx:GrammarParser.CoutContext):
        pass

    # Exit a parse tree produced by GrammarParser#cout.
    def exitCout(self, ctx:GrammarParser.CoutContext):
        pass


    # Enter a parse tree produced by GrammarParser#retst.
    def enterRetst(self, ctx:GrammarParser.RetstContext):
        pass

    # Exit a parse tree produced by GrammarParser#retst.
    def exitRetst(self, ctx:GrammarParser.RetstContext):
        pass


    # Enter a parse tree produced by GrammarParser#variablename.
    def enterVariablename(self, ctx:GrammarParser.VariablenameContext):
        pass

    # Exit a parse tree produced by GrammarParser#variablename.
    def exitVariablename(self, ctx:GrammarParser.VariablenameContext):
        pass


    # Enter a parse tree produced by GrammarParser#typename.
    def enterTypename(self, ctx:GrammarParser.TypenameContext):
        pass

    # Exit a parse tree produced by GrammarParser#typename.
    def exitTypename(self, ctx:GrammarParser.TypenameContext):
        pass


    # Enter a parse tree produced by GrammarParser#strexp.
    def enterStrexp(self, ctx:GrammarParser.StrexpContext):
        pass

    # Exit a parse tree produced by GrammarParser#strexp.
    def exitStrexp(self, ctx:GrammarParser.StrexpContext):
        pass


    # Enter a parse tree produced by GrammarParser#numeric.
    def enterNumeric(self, ctx:GrammarParser.NumericContext):
        pass

    # Exit a parse tree produced by GrammarParser#numeric.
    def exitNumeric(self, ctx:GrammarParser.NumericContext):
        pass


    # Enter a parse tree produced by GrammarParser#semicolon.
    def enterSemicolon(self, ctx:GrammarParser.SemicolonContext):
        pass

    # Exit a parse tree produced by GrammarParser#semicolon.
    def exitSemicolon(self, ctx:GrammarParser.SemicolonContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignment.
    def enterAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignment.
    def exitAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#arithmetic.
    def enterArithmetic(self, ctx:GrammarParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by GrammarParser#arithmetic.
    def exitArithmetic(self, ctx:GrammarParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by GrammarParser#star.
    def enterStar(self, ctx:GrammarParser.StarContext):
        pass

    # Exit a parse tree produced by GrammarParser#star.
    def exitStar(self, ctx:GrammarParser.StarContext):
        pass


    # Enter a parse tree produced by GrammarParser#homer.
    def enterHomer(self, ctx:GrammarParser.HomerContext):
        pass

    # Exit a parse tree produced by GrammarParser#homer.
    def exitHomer(self, ctx:GrammarParser.HomerContext):
        pass


    # Enter a parse tree produced by GrammarParser#comma.
    def enterComma(self, ctx:GrammarParser.CommaContext):
        pass

    # Exit a parse tree produced by GrammarParser#comma.
    def exitComma(self, ctx:GrammarParser.CommaContext):
        pass


    # Enter a parse tree produced by GrammarParser#unary.
    def enterUnary(self, ctx:GrammarParser.UnaryContext):
        pass

    # Exit a parse tree produced by GrammarParser#unary.
    def exitUnary(self, ctx:GrammarParser.UnaryContext):
        pass


    # Enter a parse tree produced by GrammarParser#lbra.
    def enterLbra(self, ctx:GrammarParser.LbraContext):
        pass

    # Exit a parse tree produced by GrammarParser#lbra.
    def exitLbra(self, ctx:GrammarParser.LbraContext):
        pass


    # Enter a parse tree produced by GrammarParser#rbra.
    def enterRbra(self, ctx:GrammarParser.RbraContext):
        pass

    # Exit a parse tree produced by GrammarParser#rbra.
    def exitRbra(self, ctx:GrammarParser.RbraContext):
        pass


    # Enter a parse tree produced by GrammarParser#lpar.
    def enterLpar(self, ctx:GrammarParser.LparContext):
        pass

    # Exit a parse tree produced by GrammarParser#lpar.
    def exitLpar(self, ctx:GrammarParser.LparContext):
        pass


    # Enter a parse tree produced by GrammarParser#rpar.
    def enterRpar(self, ctx:GrammarParser.RparContext):
        pass

    # Exit a parse tree produced by GrammarParser#rpar.
    def exitRpar(self, ctx:GrammarParser.RparContext):
        pass


    # Enter a parse tree produced by GrammarParser#lsq.
    def enterLsq(self, ctx:GrammarParser.LsqContext):
        pass

    # Exit a parse tree produced by GrammarParser#lsq.
    def exitLsq(self, ctx:GrammarParser.LsqContext):
        pass


    # Enter a parse tree produced by GrammarParser#rsq.
    def enterRsq(self, ctx:GrammarParser.RsqContext):
        pass

    # Exit a parse tree produced by GrammarParser#rsq.
    def exitRsq(self, ctx:GrammarParser.RsqContext):
        pass


    # Enter a parse tree produced by GrammarParser#logic.
    def enterLogic(self, ctx:GrammarParser.LogicContext):
        pass

    # Exit a parse tree produced by GrammarParser#logic.
    def exitLogic(self, ctx:GrammarParser.LogicContext):
        pass


    # Enter a parse tree produced by GrammarParser#leftarrows.
    def enterLeftarrows(self, ctx:GrammarParser.LeftarrowsContext):
        pass

    # Exit a parse tree produced by GrammarParser#leftarrows.
    def exitLeftarrows(self, ctx:GrammarParser.LeftarrowsContext):
        pass


    # Enter a parse tree produced by GrammarParser#rightarrows.
    def enterRightarrows(self, ctx:GrammarParser.RightarrowsContext):
        pass

    # Exit a parse tree produced by GrammarParser#rightarrows.
    def exitRightarrows(self, ctx:GrammarParser.RightarrowsContext):
        pass


