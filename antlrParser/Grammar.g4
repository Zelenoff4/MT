grammar Grammar;

program: gl main? eof;

eof: EOF;
gl: (strr)*;
main: 'int main()' lbra line+ rbra;
line:  (strr | ifst | forst | retst | cin | cout | simple_variable_operation );

ifst  : 'if' lpar boolex rpar lbra line* rbra ('else' lbra line* rbra)?;

boolex: expression;


arg: variablename
   | numeric
   | expression
   ;

expression: lpar expression rpar
          | op_application
          ;

simple_variable_operation: variablename (logic | arithmetic assignment| assignment) arg semicolon;

op_application: unary expression| (variablename | numeric | lpar expression rpar) (logic | arithmetic) arg;

forst: 'for' lpar strr? semicolon? boolex? semicolon (variablename arithmetic assignment (variablename | numeric))? rpar lbra line* rbra;

strr: typename variables;
variables: variable expansion;
variable: (variablename | star variable | homer variablename) (assignment (strexp | numeric | variablename ))? ;
expansion: (comma variable expansion | semicolon);

cin: 'cin' (rightarrows variablename)+ semicolon;
cout: 'cout' (leftarrows (variablename | strexp))+ semicolon;


retst: 'return 0' semicolon;

variablename: TYPENAME;
typename: TYPENAME;
strexp: STREXP;
numeric: NUMERIC;
semicolon: SEMICOLON;
assignment: ASSIGNMENT;
arithmetic: (PLUS | MINUS | STAR | DEL | HOMER | MOD | LOGOR);
star: STAR;
homer: HOMER;
comma: COMMA;
unary: UNARY;
lbra: LBRA;
rbra: RBRA;
lpar: LPAR;
rpar: RPAR;
lsq: LSQ;
rsq: RSQ;
logic: LOGIC;
leftarrows: LEFTARROWS;
rightarrows: RIGHTARROWS;



fragment LITERAL: [a-zA-Z_];
fragment DIGIT: [0-9];
STREXP: ('"' ~["]* '"' | '\'' '\\'? ~[']? '\'');
NUMERIC: DIGIT+;
TYPENAME : LITERAL (LITERAL | DIGIT)*;

RIGHTARROWS:  '>>' ;
LEFTARROWS:  '<<' ;
WHITESPACE: [ \t\r\n] -> skip;


COMMA: ',';
LPAR:  '(' ;
RPAR:  ')' ;
LBRA:  '{' ;
RBRA:  '}' ;
LSQ:  '[' ;
RSQ:  ']' ;
SEMICOLON:  ';' ;

INCDEC: '++'
      | '--'
      ;


UNARY: '~'
    | '!';


/*ARITHMETIC
    : '|'
    | '&'
    | '^'
    | '-'
    | '+'
    | '*'
    | '/'
    | '%';
*/

HOMER: '&';
STAR: '*';
PLUS: '+';
MINUS: '-';
DEL: '/';
MOD: '%';
LOGOR: '|';
ASSIGNMENT: '=';


LOGIC
    : '<'
    | '>'
    | '<='
    | '>='
    | '!='
    | '=='
    | '||'
    | '&&';