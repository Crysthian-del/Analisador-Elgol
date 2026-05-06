import ply.lex as lex

# =========================
# PALAVRAS RESERVADAS
# =========================

reservadas = {
    'elgio': 'ELGIO',
    'numero': 'NUMERO_TIPO',
    'NADA': 'NADA',
    'NEG': 'NEG',
    'EXP': 'EXP',
    'enquanto': 'ENQUANTO',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'para': 'PARA',
    'inicio': 'INICIO',
    'fim': 'FIM',
    'maior': 'MAIOR',
    'menor': 'MENOR',
    'igual': 'IGUAL',
    'diferente': 'DIFERENTE',
    'migual': 'MIGUAL',
    'Migual': 'MIGUAL2'
}

# =========================
# TOKENS
# =========================

tokens = [
    'IDENTIFICADOR',
    'FUNCAO',
    'NUMERO',

    'IGUAL_OP',
    'MOD',
    'MAIS',
    'MENOS',
    'DIV',
    'MULT',

    'LPAREN',
    'RPAREN',
    'PONTO',
    'VIRGULA'
] + list(reservadas.values())

# =========================
# OPERADORES E SIMBOLOS
# =========================

t_IGUAL_OP = r'='
t_MOD = r'%'
t_MAIS = r'\+'
t_MENOS = r'-'
t_DIV = r'/'
t_MULT = r'x'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PONTO = r'\.'
t_VIRGULA = r','

# =========================
# IGNORAR ESPAÇOS
# =========================

t_ignore = ' \t'

# =========================
# COMENTÁRIOS
# =========================

def t_COMENTARIO(t):
    r'\*.*'
    pass

# =========================
# FUNÇÕES
# =========================

def t_FUNCAO(t):
    r'_[A-Z][a-zA-Z]{2,}[a-z]'
    return t

# =========================
# IDENTIFICADORES E RESERVADAS
# =========================

def t_IDENTIFICADOR(t):
    r'[A-Z][a-zA-Z]{2,}[a-z]'

    if t.value in reservadas:
        t.type = reservadas[t.value]

    return t

# =========================
# NÚMEROS
# =========================

def t_NUMERO(t):
    r'[1-9][0-9]*'
    return t

# =========================
# QUEBRA DE LINHA
# =========================

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# =========================
# ERROS
# =========================

def t_error(t):
    print(f"Erro léxico: caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

# =========================
# BUILD DO LEXER
# =========================

lexer = lex.lex()

# =========================
# TESTE
# =========================

codigo = """
* Linguagem Elgol

numero Teste .

Lixo = 34 .

NEG Lixo .

numero _Soma (numero Numm, numero Doiss) .

Teste = 3 EXP 4 .
"""

lexer.input(codigo)

while True:
    tok = lexer.token()

    if not tok:
        break

    print(tok)
