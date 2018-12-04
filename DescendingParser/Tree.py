class Tree():
    def __init__(self, value, children):
        self.nodeValue = value
        self.kids = []
        for i in children:
            self.kids.append(i)

    def printTree(self, level = 0):
        print('\t' * level + self.nodeValue)
        for i in self.kids:
            i.printTree(level + 1)

    def equals(self, other):
        isCorrect = True
        if self.nodeValue == other.nodeValue and len(self.kids) == len(other.kids):
            for i in range(len(self.kids)):
                isCorrect &= self.kids[i].equals(other.kids[i])
        else:
            isCorrect = False
        return isCorrect