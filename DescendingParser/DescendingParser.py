from Token import Token
from LexicalAnalyzer import LexicalAnalyzer
from Tree import Tree


class Parser():
    def __init__(self, fin):
        self.analyzer = LexicalAnalyzer(fin)

    def S(self):
        if self.analyzer.curToken() == Token.n:
            kids = []
            kids.append(self.L())
            kids.append(self.S())
            return Tree("S", kids)
        elif self.analyzer.curToken() == Token.endfile:
            return Tree("S", [])
        else:
            raise ValueError("S failed with token " + self.analyzer.curToken())

    def L(self):
        if self.analyzer.curToken() == Token.n:
            kids = []
            kids.append(Tree(Token.n, []))
            self.analyzer.nextToken()
            kids.append(self.V())
            return Tree("L", kids)
        else:
            raise ValueError("L failed with token " + self.analyzer.curToken())

    def V(self):
        if self.analyzer.curToken() == Token.star:
            kids = []
            kids.append(self.VS())
            kids.append(self.N())
            return Tree("V", kids)
        elif self.analyzer.curToken() == Token.n:
            kids = []
            kids.append(self.VS())
            kids.append(self.N())
            return Tree('V', kids)
        else:
            raise ValueError("V failed with token " + self.analyzer.curToken())

    def VS(self):

        if self.analyzer.curToken() == Token.star:
            kids = []
            #kids.append(Tree(Token.star, []))
            self.analyzer.nextToken()
            kids.append(self.VS())
            return Tree(Token.star, kids)
        elif self.analyzer.curToken() == Token.n:
            kids = []
            kids.append(Tree(Token.n, []))
            self.analyzer.nextToken()
            return Tree("VS", kids)
        else:
            raise ValueError("VS failed with token " + self.analyzer.curToken())

    def N(self):

        if self.analyzer.curToken() == Token.comma:
            kids = []
            kids.append(Tree(Token.comma, []))
            self.analyzer.nextToken()
            kids.append(self.VS())
            kids.append(self.N())
            return Tree("N", kids)
        elif self.analyzer.curToken() == Token.semicolon:
            self.analyzer.token = Token.endfile
            return Tree(Token.semicolon, [])
        else:
            raise ValueError("N failed with token " + self.analyzer.curToken())

    def parse(self):
        self.analyzer.nextToken()
        return self.S()

#parser = Parser(fin)
#tree = parser.parse().printTree()
