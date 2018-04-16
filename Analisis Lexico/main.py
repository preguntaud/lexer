import ply.lex as lex

pseudocodigo = [ 'PROCESO', 'FINPROCESO', 'DEFINIR', 'COMO', 'LEER', 'ESCRIBIR', 'SI','ENTONCES','SINO','FINSI', 'PARA', 'HASTA', 'HACER', 'FINPARA', 'ASIGNACION' ]

tokens = pseudocodigo + [ 'IDENTIFICADOR','NUMBER','PLUS','MINUS','TIMES','DIVIDE','POTENCIA', 'EQUALS', 'MENORIGUAL','MENOR','MAYORIGUAL','MAYOR','DIFERENTE','PUNTOCOMA',
    'COMA','PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'COMILLA' ]

t_ignore = ' \n\t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POTENCIA = r'(\*{2} | \^)'
t_EQUALS = r':='
t_MENORIGUAL = r'<='
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MAYOR = r'>'
t_DIFERENTE = r'!='
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_COMILLA = r'\"'

def t_PROCESO(t):
    r'Proceso'
    return t

def t_FINPROCESO(t):
    r'FinProceso'
    return t

def t_DEFINIR(t):
    r'Definir'
    return t

def t_COMO(t):
    r'Como'
    return t

def t_LEER(t):
    r'Leer'
    return t

def t_ESCRIBIR(t):
    r'Escribir'
    return t

def t_SI(t):
    r'Si'
    return t

def t_ENTONCES(t):
    r'Entonces'
    return t

def t_SINO(t):
    r'Sino'
    return t

def t_FINSI(t):
    r'FinSi'
    return t

def t_PARA(t):
    r'Para'
    return t

def t_HASTA(t):
    r'Hasta'
    return t

def t_HACER(t):
    r'Hacer'
    return t

def t_FINPARA(t):
    r'FinPara'
    return t

def t_ASIGNACION(t):
    r'\<-'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

a = open("data.txt")
lineas = a.readlines()

for i in lineas:
    lex.input(i)

    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
