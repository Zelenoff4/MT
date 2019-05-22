from random import randint

from generated.GrammarParser import GrammarParser
from generated.GrammarVisitor import ParseTreeVisitor


class CustomVisitor(ParseTreeVisitor):
    wordsReplacements = dict()
    usedObfs = set()
    obfuscateLen = 5

    def rebuildVariables(self):
        for word in self.wordsReplacements:
            self.usedObfs.remove(self.wordsReplacements[word])
            newWord = self.obfuscate(word)
            self.usedObfs.add(newWord)
            self.wordsReplacements[word] = newWord

    def obfuscate(self, variable):
        literals = 'IO10'
        LIT = ['I1', 'O0']
        iterations = 0
        pos = 0
        newLen = self.obfuscateLen
        if variable == 'endl':
            return variable
        while True:
            ans = ''
            for i in range(newLen):
                if i == 0:
                    ans += 'I'
                else:
                    if pos % 2 == 0:
                        ans += LIT[0][randint(0, 1)]
                    else:
                        ans += LIT[1][randint(0, 1)]
                pos += 1
            if ans not in self.usedObfs:
                self.usedObfs.add(ans)
                self.wordsReplacements[variable] = ans
                break
            iterations += 1
            if iterations > 2 ** newLen:
                newLen += 1
                self.obfuscateLen += 1
                self.rebuildVariables()
        return ans

    def genSpamVariable(self):
        return 'string {0} = "{1}";'.format(self.obfuscate('a' * self.obfuscateLen), 'hey, im here to add some spam. Notice me!')


    @staticmethod
    def multi_match(test_list, pattern):
        if len(test_list) != len(pattern):
            return False
        return all(isinstance(elem, t) for (elem, t) in zip(test_list, pattern))

    @staticmethod
    def add_tabs(expr):
        return '\n'.join(map(lambda s: '\t' + s, expr.split('\n')))

    def visitVariablename(self, ctx: GrammarParser.VariablenameContext):
        var = ctx.getText()
        if var in self.wordsReplacements:
            var = self.wordsReplacements[var]
        else:
            var = self.obfuscate(var)
        return var

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        children = ctx.children
        if len(children) == 3:
            return '{0}{1}'.format(self.visitGl(children[0]), self.visitMain(children[1]))
        else:
            return self.visitGl(children[0])

    # Visit a parse tree produced by GrammarParser#eof.
    def visitEof(self, ctx:GrammarParser.EofContext):
        return

    # Visit a parse tree produced by GrammarParser#gl.
    def visitGl(self, ctx:GrammarParser.GlContext):
        children = ctx.children
        ans = ''
        if len(children) > 0:
            i = 0
            while i < len(children):
                ans += self.visitStrr(children[i]) + '\n'
                i += 1
        return ans

    # Visit a parse tree produced by GrammarParser#main.
    def visitMain(self, ctx:GrammarParser.MainContext):
        ans = 'int main(){\n'
        children = ctx.children
        for i in range(2, len(children) - 1):
            ans += self.visitLine(children[i]) + '\n'
        ans += '}'
        return ans

    # Visit a parse tree produced by GrammarParser#line.
    def visitLine(self, ctx:GrammarParser.LineContext):
        kid = ctx.children[0]
        if isinstance(kid, GrammarParser.StrrContext):
            return self.visitStrr(kid)
        elif isinstance(kid, GrammarParser.IfstContext):
            return self.visitIfst(kid)
        elif isinstance(kid, GrammarParser.ForstContext):
            return self.visitForst(kid)
        elif isinstance(kid, GrammarParser.RetstContext):
            return self.visitRetst(kid)
        elif isinstance(kid, GrammarParser.Simple_variable_operationContext):
            return self.visitSimple_variable_operation(kid)
        elif isinstance(kid, GrammarParser.CinContext):
            return self.visitCin(kid)
        else:
            return self.visitCout(kid)

    # Visit a parse tree produced by GrammarParser#ifst.
    def visitIfst(self, ctx:GrammarParser.IfstContext):
        children = ctx.children
        ans = 'if ('
        ans += self.visitBoolex(children[2]) + '){\n'
        i = 5
        while isinstance(children[i], GrammarParser.LineContext):
            ans += self.visitLine(children[i]) + '\n'
            i += 1
        ans += '}'
        i += 1
        if len(children) > i:
            ans += ' else {\n'
            i += 2
            while isinstance(children[i], GrammarParser.LineContext):
                ans += self.visitLine(children[i]) + '\n'
                i += 1
            ans += '}'
        return ans

    # Visit a parse tree produced by GrammarParser#boolex.
    def visitBoolex(self, ctx:GrammarParser.BoolexContext):
        return self.visitExpression(ctx.children[0])

    # Visit a parse tree produced by GrammarParser#arg.
    def visitArg(self, ctx:GrammarParser.ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        children = ctx.children
        if self.multi_match(children, [GrammarParser.Op_applicationContext]):
            return self.visitOp_application(children[0])
        else:
            return '({0})'.format(self.visitOp_application(children[1]))

    # Visit a parse tree produced by GrammarParser#simple_variable_operation.
    def visitSimple_variable_operation(self, ctx: GrammarParser.Simple_variable_operationContext):
        children = ctx.children
        ans = self.visitVariablename(children[0])
        i = 1
        if isinstance(children[i], GrammarParser.LogicContext):
            ans += self.visitLogic(children[i])
        elif isinstance(children[i], GrammarParser.ArithmeticContext):
            ans += '{0}{1}'.format(self.visitArithmetic(children[i]), self.visitAssignment(children[i + 1]))
            i += 1
        else:
            ans += self.visitAssignment(children[i])
        i += 1
        return '{0}{1}{2}'.format(ans, self.visitArg(children[i]), ';')

    # Visit a parse tree produced by GrammarParser#op_application.
    def visitOp_application(self, ctx:GrammarParser.Op_applicationContext):
        children = ctx.children
        if self.multi_match(children, [GrammarParser.UnaryContext, GrammarParser.ExpressionContext]):
            return '{0}{1}'.format(self.visitUnary(children[0]), self.visitExpression(children[1]))
        elif len(children) == 3:
            if isinstance(children[0], GrammarParser.VariablenameContext):
                if isinstance(children[1], GrammarParser.LogicContext):
                    return '{0}{1}{2}'.format(self.visitVariablename(children[0]), self.visitLogic(children[1]), self.visitArg(children[2]))
                else:
                    return '{0}{1}{2}'.format(self.visitVariablename(children[0]), self.visitArithmetic(children[1]), self.visitArg(children[2]))
            elif isinstance(children[0], GrammarParser.NumericContext):
                if isinstance(children[1], GrammarParser.LogicContext):
                    return '{0}{1}{2}'.format(self.visitNumeric(children[0]), self.visitLogic(children[1]), self.visitArg(children[2]))
                else:
                    return '{0}{1}{2}'.format(self.visitNumeric(children[0]), self.visitArithmetic(children[1]), self.visitArg(children[2]))
            else:
                if isinstance(children[3], GrammarParser.LogicContext):
                    return '{0}{1}{2}{3}{4}'.format(self.visitLpar(children[0]), self.visitExpression(children[1]), self.visitRpar(children[2]), self.visitLogic(children[3]), self.visitArg(children[4]))
                else:
                    return '{0}{1}{2}{3}{4}'.format(self.visitLpar(children[0]), self.visitExpression(children[1]), self.visitRpar(children[2]), self.visitArithmetic(children[3]), self.visitArg(children[4]))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by GrammarParser#forst.
    def visitForst(self, ctx:GrammarParser.ForstContext):
        children = ctx.children
        ans = 'for ('
        i = 2
        if isinstance(children[i], GrammarParser.StrrContext):
            ans += self.visitStrr(children[i])
        else:
            ans += ';'
        i += 1
        if isinstance(children[i], GrammarParser.BoolexContext):
            ans += self.visitBoolex(children[i])
            i += 1
        ans += ';'
        i += 1
        if isinstance(children[i], GrammarParser.VariablenameContext):
            ans += '{0}{1}{2}'.format(self.visitVariablename(children[i]), self.visitArithmetic(children[i + 1]), self.visitAssignment(children[i + 2]))
            i += 3
            if isinstance(children[i], GrammarParser.VariablenameContext):
                ans += self.visitVariablename(children[i])
            else:
                ans += self.visitNumeric(children[i])
            i += 1
        ans += '){\n'
        i += 2
        while isinstance(children[i], GrammarParser.LineContext):
            ans += self.visitLine(children[i]) + '\n'
            i += 1
        ans += '}'
        return ans


    # Visit a parse tree produced by GrammarParser#cin.
    def visitCin(self, ctx:GrammarParser.CinContext):
        children = ctx.children
        i = 1
        ans = 'cin '
        while isinstance(children[i], GrammarParser.RightarrowsContext):
            ans += '{0} {1}'.format(self.visitRightarrows(children[i]), self.visitVariablename(children[i + 1]))
            i += 2
        ans += ';'
        return '{0}\n{1}'.format(ans, self.genSpamVariable())

    # Visit a parse tree produced by GrammarParser#cout.
    def visitCout(self, ctx:GrammarParser.CoutContext):
        children = ctx.children
        i = 1
        ans = 'cout'
        while isinstance(children[i], GrammarParser.LeftarrowsContext):
            ans += self.visitLeftarrows(children[i])
            i += 1
            if isinstance(children[i], GrammarParser.VariablenameContext):
                ans += ' ' + self.visitVariablename(children[i])
            else:
                ans += ' ' + self.visitStrexp(children[i])
            i += 1
        ans += ';'
        return '{0}\n{1}'.format(ans, self.genSpamVariable())

    # Visit a parse tree produced by GrammarParser#retst.
    def visitRetst(self, ctx:GrammarParser.RetstContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#typename.
    def visitTypename(self, ctx:GrammarParser.TypenameContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#strexp.
    def visitStrexp(self, ctx:GrammarParser.StrexpContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#numeric.
    def visitNumeric(self, ctx:GrammarParser.NumericContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#semicolon.
    def visitSemicolon(self, ctx:GrammarParser.SemicolonContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#assignment.
    def visitAssignment(self, ctx:GrammarParser.AssignmentContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#arithmetic.
    def visitArithmetic(self, ctx:GrammarParser.ArithmeticContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#star.
    def visitStar(self, ctx:GrammarParser.StarContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#homer.
    def visitHomer(self, ctx:GrammarParser.HomerContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#comma.
    def visitComma(self, ctx:GrammarParser.CommaContext):
        return ctx.getText() + ' '

    # Visit a parse tree produced by GrammarParser#unary.
    def visitUnary(self, ctx:GrammarParser.UnaryContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#lbra.
    def visitLbra(self, ctx: GrammarParser.LbraContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#rbra.
    def visitRbra(self, ctx: GrammarParser.RbraContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#lpar.
    def visitLpar(self, ctx: GrammarParser.LparContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#rpar.
    def visitRpar(self, ctx: GrammarParser.RparContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#lsq.
    def visitLsq(self, ctx: GrammarParser.LsqContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#rsq.
    def visitRsq(self, ctx: GrammarParser.RsqContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#logic.
    def visitLogic(self, ctx: GrammarParser.LogicContext):
        return ctx.getText()

    # Visit a parse tree produced by GrammarParser#leftarrows.
    def visitLeftarrows(self, ctx: GrammarParser.LeftarrowsContext):
        return ' '+ ctx.getText()

    # Visit a parse tree produced by GrammarParser#rightarrows.
    def visitRightarrows(self, ctx: GrammarParser.RightarrowsContext):
        return ' ' + ctx.getText()

    # Visit a parse tree produced by GrammarParser#strr.
    def visitStrr(self, ctx:GrammarParser.StrrContext):
        return '{0} {1}'.format(self.visitTypename(ctx.children[0]), self.visitVariables(ctx.children[1]))


    # Visit a parse tree produced by GrammarParser#variables.
    def visitVariables(self, ctx:GrammarParser.VariablesContext):
        return '{0}{1}'.format(self.visitVariable(ctx.children[0]), self.visitExpansion(ctx.children[1]))

    # Visit a parse tree produced by GrammarParser#variable.
    def visitVariable(self, ctx:GrammarParser.VariableContext):
        children = ctx.children
        if len(children) == 1:
            return self.visitVariablename(children[0])
        elif len(children) == 2:
            if self.multi_match(children, [GrammarParser.StarContext, GrammarParser.VariableContext]):
                return '{0}{1}'.format(self.visitStar(children[0]), self.visitVariable(children[1]))
            else:
                return '{0}{1}'.format(self.visitHomer(children[0]), self.visitVariablename(children[1]))
        else:
            if len(children) == 3:
                if isinstance(children[2], GrammarParser.StrexpContext):
                    return '{0}{1}{2}'.format(self.visitVariablename(children[0]), children[1].getText(), children[2].getText())
                elif isinstance(children[2], GrammarParser.NumericContext):
                    return '{0}{1}{2}'.format(self.visitVariablename(children[0]), children[1].getText(), children[2].getText())
                else:
                    return '{0}{1}{2}'.format(self.visitVariablename(children[0]), self.visitAssignment(children[1]), self.visitVariablename(children[2]))
            elif self.multi_match(children[:2], [GrammarParser.StarContext, GrammarParser.VariableContext]):
                if isinstance(children[3], GrammarParser.StrexpContext):
                    return '{0}{1}{2}{3}'.format(self.visitStar(children[0]), self.visitVariable(children[1]), self.visitAssignment(children[2]), self.visitStrexp(children[3]))
                elif isinstance(children[3], GrammarParser.NumericContext):
                    return '{0}{1}{2}{3}'.format(self.visitStar(children[0]), self.visitVariable(children[1]),
                                                 self.visitAssignment(children[2]), self.visitNumeric(children[3]))
                else:
                    return '{0}{1}{2}{3}'.format(self.visitStar(children[0]), self.visitVariable(children[1]),
                                                 self.visitAssignment(children[2]), self.visitVariablename(children[3]))
            else:
                if isinstance(children[3], GrammarParser.StrexpContext):
                    return '{0}{1}{2}{3}'.format(self.visitHomer(children[0]), self.visitVariablename(children[1]),
                                                 self.visitAssignment(children[2]), self.visitStrexp(children[3]))
                elif isinstance(children[3], GrammarParser.NumericContext):
                    return '{0}{1}{2}{3}'.format(self.visitHomer(children[0]), self.visitVariablename(children[1]),
                                                 self.visitAssignment(children[2]), self.visitNumeric(children[3]))
                else:
                    return '{0}{1}{2}{3}'.format(self.visitHomer(children[0]), self.visitVariablename(children[1]),
                                                 self.visitAssignment(children[2]), self.visitVariablename(children[3]))

    # Visit a parse tree produced by GrammarParser#expansion.
    def visitExpansion(self, ctx:GrammarParser.ExpansionContext):
        children = ctx.children
        if self.multi_match(children, [GrammarParser.SemicolonContext]):
            return self.visitSemicolon(children[0])
        else:
            return '{0}{1}{2}'.format(self.visitComma(children[0]), self.visitVariable(children[1]), self.visitExpansion(children[2]))
