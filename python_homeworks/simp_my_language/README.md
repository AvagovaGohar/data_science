THE NAME OF MY PROGRAMMING LANGUAGE: SIMP

SUPPORTING OPERATIONS: 
    if, while, variable declaration, variable assigment, complex expressions, print, arithmetic / logic operations, comments
SOME RULES:
    GENERAL:    
        Between every word or sign should be at least one space.
    IF and WHILE: 
        Body of 'if' / 'while' writes in '{', '}' scopes, '{' scope should be at the end of condition, '}' scope should be alone on line.
    COMPLEX EXPRESSIONS: (also ARITHMETIC, RELATIONAL, LOGICAL, BITWISE and ASSIGMENT operators):
        Arithmetic operators: 
            '+', '-', '*', '/', '%'
        Relational operations:
            '==', '!=', '>', '<', '>=', '<='
        Logical operators: 
            '||', '&&'
        Bitwise operations:
            '|', '&'
        Assigment operators: 
            '=', '+=', '-=', '*=', '/=', '|=', '&=', '%='

        In complex expressions you cannot use '(', ')' and there is no priority in operators. They are executed from left to right.
    SUPPORT TYPES:
        Variable declaration starts with word 'var'. The type of the variable depends on the argument, it can be changed on any other type and it cannot declarated twice (or more) .
        Types: unsigned int,unsigned float, string, bool
    COMMENTS:
        In order to write a comment, the line must begin with '//'


EXAMPLE:


var i = 0
var sum = 0
while i < 10 {
	if i >= 2 {
        print i + "_"
	}
    i += 1
    sum += i
}
if true || i {
    i = 0
    print "i = " + i
}

Output: 2 3 4 5 6 7 8 9 i = 0
