from dados import produtos, pessoas, lista

# nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5]

"""
def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
    return True

nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print()
"""

def filtra2(pessoas):
    if pessoas['idade'] < 18:
        return True

nova_lista = filter(filtra2, pessoas)

for pessoa in nova_lista:
    print(pessoa)
