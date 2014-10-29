from sys import *

lexeme = ['']*100
fo = None
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF =-1
MULT_OP = 23
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
nextToken = 1
nextChar = ""
lexeme = 0



def main():
    global fo,nextToken,charClass,lexLen,nextChar
    try:
        try:
            fo = open("input.txt", "r")                  
        except Exception, e:
            print "ERROR: cannot open input.txt"
        finally:
            getChar()
            i = 0
        while nextToken != EOF:      
            lex() 
            i+=1
        fo.close()
    except Exception, e:
        print e

def addChar():
    global fo,nextToken,charClass,lexLen,lexeme,nextChar
    if lexLen <= 98:       
        lexeme[lexLen + 1] = nextChar
        lexeme[lexLen] = 0
    else:
        print "Error:lexeme is too long."
    
def getChar():
    global fo,nextToken,charClass,lexLen,nextChar
    try:
        w = fo.read(1)
        if w != "-1":
            nextChar = w
            if nextChar.isalpha():
                charClass = LETTER
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN            
        else:
            charClass = EOF
            nextChar = '\0'        
    except Exception, e:
        print e
    
def getNonBlank():
    global fo,nextToken,charClass,lexLen,nextChar
    while nextChar.isspace():
        getChar()

def lookup(ch):      
    global fo,nextToken,charClass,lexLen,lexeme,nextChar
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
    
    
def lex():
    global fo,nextToken,charClass,lexLen,lexeme,nextChar
    lexLen = 0
    lexeme = ['']*100
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()        
        while charClass == LETTER:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[1] = 'EOF'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '\0'
  
    if nextToken!=-1:
	    print "Next token is: " + str(nextToken) + " Next lexeme is " + str(lexeme[1])
    else:
	    print "Next token is: " + str(nextToken) + " Next lexeme is EOF"


main()