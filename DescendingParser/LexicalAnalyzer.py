from Token import Token


class LexicalAnalyzer:
    token = Token()

    def __init__(self, inputFile):
        self.fin = inputFile
        self.curInd = 0
        self.nextChar()

    def isBlank(self, c):
        return c == ' ' or c == '\r' or c == '\n' or c == '\t'

    def isLetter(self, c):
        alph = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890_'
        return c in alph

    def nextChar(self):
        self.curInd += 1
        try:
            self.curChar = self.fin.read(1)
        except:
            print("Error occured while reading the file", self.fin)


    def nextToken(self):
        while (self.isBlank(self.curChar)):
            self.nextChar()
        if self.isLetter(self.curChar):
            while self.isLetter(self.curChar):
                self.nextChar()
            self.token = Token.n
        elif self.curChar == '*':
            #while self.curChar == '*':
            self.nextChar()
            self.token = Token.star
        elif self.curChar == ',':
            self.token = Token.comma
            self.nextChar()
        elif self.curChar == ';':
            self.token = Token.semicolon
        elif self.curChar == '':
            self.token = Token.endfile
        else:
            raise ValueError()


    def curToken(self):
        return self.token

    def curPos(self):
        return self.curInd
