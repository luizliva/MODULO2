"""
função executando duas funções de valores diferentes
"""

def mestre(func, *args, **kwargs):
    return func(*args, **kwargs)

def funcao(nome):
    return f'Oi {nome}!'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

exe = mestre(funcao, 'Luiz')
exe2 = mestre(saudacao, 'Luiz', saudacao='Opa bão')
print(exe)
print(exe2)