lista = [0, 1, 1, 1, 0, 0, 1, 0, 2, 2, 2, 3, 3]
contadores = []

for categoria in range(4):
    cont = 0
    for indice in lista:
        if indice == categoria:
            cont += 1
    contadores.append(cont)

print(contadores)
