grammar ConfigLang;

// --- Parser Rules ---

config: (statement)* EOF;

statement: constantDeclaration | value;

constantDeclaration: CONST NAME EQUALS value;

value: dictionary | array | NUMBER | constantExpression;

dictionary: LBRACE (pair (COMMA pair)*)? RBRACE;

pair: NAME COLON value;

array: HASH_LPAREN (value (COMMA value)*)? RPAREN;

constantExpression: DOLLAR expression DOLLAR;

// Expression rules for constant calculation (infix: +, -, len())
expression: sum;

sum: product ((PLUS | MINUS) product)*;

product: atom;

atom: NAME | NUMBER | functionCall | LPAREN sum RPAREN;

functionCall: LEN LPAREN (NAME | array | dictionary) RPAREN;


// --- Lexer Rules ---

// Keywords
CONST: 'const';
LEN: 'len';

// Data Types
NAME: [_A-Z] [_a-zA-Z0-9]*;
NUMBER: [0-9]* '.' [0-9]+; // \d*\.\d+

// Operators and Delimiters
PLUS: '+';
MINUS: '-';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
HASH_LPAREN: '#(';
COLON: ':';
COMMA: ',';
DOLLAR: '$';
EQUALS: '=';

// Comments and Whitespace
COMMENT: ';' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
