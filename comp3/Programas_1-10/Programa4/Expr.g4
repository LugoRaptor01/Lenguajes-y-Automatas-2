grammar Expr ;
root : expr EOF ;

expr : IF ID MAYOR NUM;

IF: 'if';
ID: [a-zA-Z]+;
MAYOR: '>';

NUM: [0-9]+;

WS: [ \t\r\n] + -> skip;