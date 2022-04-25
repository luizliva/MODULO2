from dados import produtos, pessoas, lista

nomes = map(lambda p: p['nome'], pessoas)

for pessoas in nomes:
    print(pessoas)