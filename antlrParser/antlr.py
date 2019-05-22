import sys
from antlr4 import *

from generated.GrammarLexer import GrammarLexer
from generated.GrammarParser import GrammarParser
from CustomVisitor import CustomVisitor


def main(argv):
    output_file_name = argv[2]
    with open(output_file_name, 'w') as output_file:
        result = solve(argv)
        output_file.writelines(result)


def solve(argv):
    data_stream = FileStream(argv[1])
    lexer = GrammarLexer(data_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.program()
    visitor = CustomVisitor()
    return visitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
