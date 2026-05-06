import re

RESERVADAS = {
    "elgio", "numero", "NADA", "NEG", "EXP",
    "enquanto", "se", "entao", "senao", "para",
    "inicio", "fim",
    "maior", "menor", "igual", "diferente", "migual", "Migual"
}

OPERADORES = {"=", "EXP", "%", "+", "-", "/", "x"}
SIMBOLOS = {"(", ")", ".", ","}

def is_identificador(token):
    return re.match(r'^[A-Z][a-zA-Z]{2,}[a-z]$', token)

def is_funcao(token):
    return re.match(r'^_[A-Z][a-zA-Z]{2,}[a-z]$', token)

def is_numero(token):
    return re.match(r'^[1-9][0-9]*$', token)

def analisar_linha(linha):
    tokens = []
    
    # remover comentário
    linha = linha.split('*')[0]

    partes = linha.replace("(", " ( ").replace(")", " ) ") \
                  .replace(".", " . ").replace(",", " , ").split()

    for token in partes:
        if token in RESERVADAS:
            tokens.append(("RESERVADA", token))

        elif token in OPERADORES:
            tokens.append(("OPERADOR", token))

        elif token in SIMBOLOS:
            tokens.append(("SIMBOLO", token))

        elif is_funcao(token):
            tokens.append(("FUNCAO", token))

        elif is_identificador(token):
            tokens.append(("IDENTIFICADOR", token))

        elif is_numero(token):
            tokens.append(("NUMERO", token))

        else:
            tokens.append(("ERRO", token))

    return tokens


def analisar_codigo(codigo):
    for i, linha in enumerate(codigo.split('\n'), 1):
        tokens = analisar_linha(linha)
        print(f"Linha {i}: {tokens}")


# TESTE
codigo = """
numero Teste .
Lixo = 34 .
NEG Lixo .
"""

analisar_codigo(codigo)