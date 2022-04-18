"""
função1 com função2 como parâmetro
"""

def func():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

exe = mestre(func)

print(exe)