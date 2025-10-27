import ply.lex as lex


tokens = ('NUM', 'PA', 'PF', 'OP')

t_NUM = r'\d+'
t_PA = r'\('
t_PF = r'\)'
t_OP = r'[\+\-\*\/]'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()


## Gramática

# P1: Exp      --> Termo SomaMenos
# P2: SomaMenos  --> '+' Termo SomaMenos
# P3:           | '-' Termo SomaMenos
# P4:           | ε
# P5: Termo    --> NumPar MultDiv
# P6: MultDiv  --> '*' NumPar MultDiv
# P7:           | '/' NumPar MultDiv
# P8:           | ε
# P9: NumPar       --> NUM
# P10:          | '(' Exp ')'

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb and prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

def rec_NumPar():
    if prox_simb is None:
        parserError(prox_simb)
    elif prox_simb.type == 'NUM':
        print("Derivando por # P10: NumPar --> NUM")
        rec_term('NUM')
        print("Reconheci # P10: NumPAr --> NUM")
    elif prox_simb.type == 'PA':
        print("Derivando por # P10: NumPar --> '(' Exp ')'")
        rec_term('PA')
        rec_Exp()
        rec_term('PF')
        print("Reconheci # P10: NumPar --> '(' Exp ')'")
    else: 
        parserError(prox_simb)

def rec_MultDiv():
    if prox_simb and prox_simb.type == 'OP':
        if prox_simb.value =='*':
            print("Derivando por # P6: MultDiv  --> '*' NumPar MultDiv")
            rec_term('OP')
            rec_NumPar()
            rec_MultDiv()
            print("Reconheci # P6: MultDiv  --> '*' NumPar MultDiv")
        elif prox_simb.value == '/':
            print("Derivando por # P7: MultDiv --> '/' NumPar MultDiv")
            rec_term('OP')
            rec_NumPar()
            rec_MultDiv()
            print("Reconheci # P7: MultDiv --> '/' NumPar MultDiv")
    else :
        print("Derivando por # P8: MultDiv --> ε")
        print("Reconheci # P8: MultDiv --> ε")

def rec_Termo():
    print("Derivando por # P5: Termo --> NumPar MultDiv")
    rec_NumPar()
    rec_MultDiv()
    print("Reconheci # P5: Termo --> NumPar MultDiv")

def rec_SomaMenos():
    global prox_simb
    if prox_simb and prox_simb.type == 'OP':
        if prox_simb.value == '+':
            print("Derivando por # P2: SomaMenos --> '+' Termo SomaMenos")
            rec_term('OP')
            rec_Termo()
            rec_SomaMenos()
            print("Reconheci # P2: SomaMenos --> '+' Termo SomaMenos")
        elif prox_simb.value == '-':
            print("Derivando por # P3: SomaMenos --> '-' Termo SomaMenos")
            rec_term('OP')
            rec_Termo()
            rec_SomaMenos()
            print("Reconheci # P2: SomaMenos --> '-' Termo SomaMenos")
    else:
        print("Derivando por # P4: SomaMenos --> ε")
        print("Reconheci # P4: SomaMenos --> ε")

def rec_Exp():
    print("Derivando por # P1: Exp --> Termo SomaMenos")
    rec_Termo()
    rec_SomaMenos()
    print("Reconheci # P1: Exp --> Termo SomaMenos")


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Exp()
    if prox_simb is not None:
        print(f"Tokens restantes: {prox_simb}")
    else: print("That's all folks!")

linha = input("Introduza uma Expressão: ")
rec_Parser(linha)

