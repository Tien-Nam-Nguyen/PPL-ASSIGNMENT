//2011652
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


//program  : mptype 'main' LB RB LP body? RP EOF ;
program: classDecls EOF;
classDecls: classDecl classDecls | classDecl;
classDecl: CLASS ID (EXTENDS ID)? LP memberListNoNull? RP;
memberListNoNull: (classAttr|classMethod)+;

classAttr: (FINAL|STATIC|STATIC FINAL|FINAL STATIC)? typ attrDecls SEMI;
attrDecls:  attrDecl COMMA attrDecls | attrDecl;
attrDecl: ID ('=' expr)?;

classMethod: STATIC? methodtype ID LB params? RB blockStmt | constructor;
constructor: ID LB params? RB blockStmt;
params: param SEMI params | param;
param: typ ids;
ids: ID COMMA ids | ID;


blockStmt: LP varDecls? stmts? RP;
varDecls: varDecl varDecls | varDecl;
varDecl: FINAL? typ listVar SEMI;
listVar: ID ('=' expr)? COMMA listVar | ID ('=' expr)?;

stmts: stmt stmts | stmt;
stmt: blockStmt|assignStmt|ifStmt|forStmt|breakStmt|contiStmt|returnStmt|invoStmt;
assignStmt: lhs ASS expr SEMI;
lhs: ID | expr8; 		//20/10 thay ID|expr8 bang
ifStmt: IF expr THEN stmt (ELSE stmt)?;
forStmt: FOR ID ASS expr (TO|DOWNTO) expr DO stmt;
breakStmt: BREAK SEMI;
contiStmt: CONTINUE SEMI;
returnStmt: RETURN expr SEMI;
invoStmt: (expr9 DOT ID LB exprs? RB) SEMI;				//20/10 thay (expr9) bang expr8




expr: expr1 (GT|LT|GT_EQ|LT_EQ) expr1 | expr1;
expr1: expr2 (EQ|NOT_EQ) expr2 | expr2;
expr2: expr2 (AND|OR) expr3 | expr3;
expr3: expr3 (ADD|SUB) expr4 | expr4;
expr4: expr4 (MUL|INT_DIV|FLOAT_DIV|MOD) expr5 | expr5;
expr5: expr5 CONCAT expr6 | expr6;
expr6: NOT expr6 | expr7;
expr7: (ADD|SUB) expr7 | expr8;
expr8: expr9 LSQB expr RSQB |expr9;					//bo attOrMethod, array chua literal ko phai class
expr9: expr9 DOT ID | expr9 DOT ID LB exprs? RB| expr10;
expr10: NEW ID LB exprs? RB | expr11;
expr11: ID|INTLIT|FLOATLIT|STRINGLIT|BOOLIT|NIL|sube|THIS|arraylit;
sube: LB expr RB;

exprs: expr COMMA exprs | expr;		//No empty list of expression


arraytype: (INTTYPE|FLOATTYPE|STRING|BOOLEAN|ID) LSQB INTLIT RSQB;	//ID la class,   change ARRAYTYPE to arraytype
ptype: (INTTYPE|FLOATTYPE|STRING|BOOLEAN|arraytype);
typ: ptype | ID;
methodtype: typ | VOIDTYPE;

INTLIT: [0-9]+;

FLOATLIT: INTPART (DECIPART EXPPART? | EXPPART);
fragment INTPART: [0-9]+;
fragment DECIPART: '.'[0-9]*;
fragment EXPPART: [eE] ('+'|'-')? [0-9]+;

BOOLIT: (TRUE | FALSE);

STRINGLIT: '"' CHAR* '"';
fragment CHAR: (~[\f\r\n\\"] | '\\'[bfrnt"\\]);

arraylit: LP ele_list RP;
ele: (INTLIT|FLOATLIT|STRINGLIT|BOOLIT);
ele_list: ele COMMA ele_list | ele;


//some reserved keyword must to be matched first
WRITELN: ('WriteLn'|'writeln'|'WRITELN');
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOATTYPE: 'float';
IF: 'if';
INTTYPE: 'int' ;
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
VOIDTYPE: 'void'  ;
TRUE: 'true';
FALSE: 'false';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto'; 


//some operator need to be matched first
ADD: '+';
SUB: '-';
MUL: '*';
FLOAT_DIV: '/';
INT_DIV: '\\';
MOD: '%';
NOT_EQ: '!=';
EQ: '==';
LT: '<';
GT: '>';
LT_EQ: '<=';
GT_EQ: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCAT: '^';

LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
COMMA: ',';
LSQB: '[';
RSQB: ']';
DOT: '.';
SEMI: ';' ;
COLON: ':';
ASS: ':=';




ID: [a-zA-Z_][a-zA-Z_0-9]* ; 	//ID is also a classname





BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '#'~[\r\n\f]* -> skip;


WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines


UNCLOSE_STRING: '"' CHAR* (EOF? | ~'"') {
	if self.text[-1] in ['\r','\n']:
		raise UncloseString(self.text[0:-1])
	else: raise UncloseString(self.text[0:])
}; 

ILLEGAL_ESCAPE: '"' CHAR* '\\' ~[bfrnt"\\]{
	raise IllegalEscape(self.text[0:])
};
ERROR_CHAR: .{raise ErrorToken(self.text)};
