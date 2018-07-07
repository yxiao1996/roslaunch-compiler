from ply import *
import lex

tokens = lex.tokens

print (tokens)

# This catch-all rule is used for any catastrophic errors.  In this case,
# we simply return nothing

precedence = (
    ('right', 'DIVIDE'),
)


def p_module(p):
    #'''module : MODULE LPAREN input output RPAREN'''
    '''module : MODULE name LPAREN input_list output_list node_list assign_list RPAREN'''
    p[0] = {}
    p[0]['name'] = p[2]
    p[0]['input'] = p[4]
    p[0]['output'] = p[5]
    p[0]['node'] = p[6]
    p[0]['assign'] = p[7]

def p_program_error(p):
    '''module : error'''
    p[0] = None
    p.parser.error = 1

def p_input(p):
    '''input : INPUT topic'''
    p[0] = p[2]

def p_input_list(p):
    '''input_list : input_list input
                  | input'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]

def p_output(p):
    '''output : OUTPUT topic'''
    p[0] = p[2]

def p_output_list(p):
    '''output_list : output_list output
                   | output'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]

def p_node(p):
    '''node : NODE LPAREN node_info RPAREN'''
    p[0] = p[3]

def p_node_info(p):
    '''node_info : NAME name input_list output_list pack exec'''
    p[0] = {}
    p[0]['name'] = p[2]
    p[0]['input'] = p[3]
    p[0]['output'] = p[4]
    p[0]['pack'] = p[5]
    p[0]['exec'] = p[6]

def p_node_list(p):
    '''node_list : node_list node
                 | node'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]

def p_exec(p):
    '''exec : EXEC name'''
    p[0] = p[2]

def p_pack(p):
    '''pack : PACK name'''
    p[0] = p[2]

def p_assign(p):
    '''assign : ASSIGN topic EQUALS topic'''
    p[0] = {}
    p[0]['pub'] = p[2]
    p[0]['sub'] = p[4]

def p_assign_list(p):
    '''assign_list : assign_list assign
                   | assign'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[2])
    else:
        p[0] = [p[1]]

def p_topic(p):
    '''topic : topic DIVIDE name
             | DIVIDE name'''
    if len(p) == 3:
        p[0] = '/' + str(p[2])
    elif len(p) == 4:
        p[0] = p[1] + '/' + p[3]

def p_name(p):
    '''name : ID'''
    p[0] = p[1]

def p_empty(p):
    '''empty : '''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("SYNTAX ERROR AT EOF")

parser = yacc.yacc()

def parse(data, debug=2):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p

if __name__ == "__main__":
    data = '''MODULE foo(  
                INPUT /a/c
                INPUT /e/f
                OUTPUT /b/d
                OUTPUT /g/h
                NODE(
                    NAME bar
                    INPUT /i
                    OUTPUT /j
                    PACK test0
                    EXEC test0.py
                )
                NODE(
                    NAME foo
                    INPUT /m
                    OUTPUT /n
                    PACK test1
                    EXEC test1.py
                )
                ASSIGN /c = /d
                ASSIGN /e = /f
            )'''

    # Give the lexer some input
    #lex.lex.input(data)

    # Tokenize
    #while True:
    #    tok = lex.lex.token()
    #    if not tok: 
    #        break      # No more input
    #    print(tok)

    result = parse(data)
    print(result)
