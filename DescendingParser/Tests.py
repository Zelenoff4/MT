from DescendingParser import Parser


def createFile(test):
    f = open("/home/zelenoff/PycharmProjects/DescendingParser/input.txt", 'w+')
    f.write(test)
    f.close()
    return f


def singleVar():
    test = 'int a;'
    print("Running test -> ", test)
    file = open(createFile(test).name)
    Parser(file).parse().printTree()
    print('==================================')
    file.close()


def singlePointVar():
    test = 'char *a;'
    print("Running test -> ", test)
    file = open(createFile(test).name)
    Parser(file).parse().printTree()
    print('==================================')
    file.close()


def multipleVars():
    test = 'long *b, ***a, c, d3;'
    print("Running test -> ", test)
    file = open(createFile(test).name)
    Parser(file).parse().printTree()
    print('==================================')
    file.close()

def multipleVarsAndTabulations():
    test = '        \n  int *   *bc, d      , ****d\n;'
    print("Running test -> ", test)
    file = open(createFile(test).name)
    Parser(file).parse().printTree()
    print('==================================')
    file.close()


def runTests():
    singleVar()
    singlePointVar()
    multipleVars()
    multipleVarsAndTabulations()


runTests()
