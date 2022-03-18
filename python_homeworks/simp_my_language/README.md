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
	You cannot use '(', ')' in complex expressions, and there is no precedence in operators. They run from left to right.
    SUPPORT TYPES:
        A variable declaration starts with the word 'var'. The type of a variable depends on the argument, it can be changed to any other type, and it cannot be declared twice (or more).
        Types: unsigned int, unsigned float, string, bool
    COMMENTS:
        To write a comment, the line must start with '//'


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
