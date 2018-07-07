from ply import *

keywords = (
    'MODULE',
    'INPUT', 'OUTPUT', 'NODE',
    'PACK', 'EXEC', 'NAME',
    'ASSIGN'
)

tokens = keywords + (
    'EQUALS', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'ID', 'NEWLINE'
)

t_ignore = ' \t'

t_EQUALS = r'='
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9.]*'
    if t.value in keywords:
        t.type = t.value
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    #return t

def t_error(t):
    print("Illegal charactor %s" % t.value[0])

lex.lex(debug=0)

if __name__ == "__main__":
    data = '''
    module (
        input /cam
        output /crop

        node (
            pack cam
            exce cam
        )

        assign /cam = /crop
    )
    '''

    # Give the lexer some input
    lex.input(data)

    # Tokenize
    while True:
        tok = lex.token()
        if not tok: 
            break      # No more input
        print(tok)