def categoriaAcidez(valorAcidez):
    if 5.5 < valorAcidez <= 6.5:
        catAcidez = 3
    elif (6.5 < valorAcidez <= 7.0) or (5.0 < valorAcidez <= 5.5):
        catAcidez = 2
    elif (7.0 < valorAcidez <= 8.0) or (4.5 <= valorAcidez <= 5.0):
        catAcidez = 1
    elif valorAcidez > 8.0 or valorAcidez < 4.5:
        catAcidez = 0

    return catAcidez


def categoriaMateria(valorMateria):
    if valorMateria < 3:
        catMateria = 0
    elif valorMateria <= 4:
        catMateria = 1
    elif valorMateria <= 5:
        catMateria = 2
    elif valorMateria > 5:
        catMateria = 3

    return catMateria


def categoriaResultante(cateMateria, cateAcidez):
    if cateMateria == cateAcidez:
        categoriaDefinitiva = cateAcidez
    else:
        # si son diferentes
        if cateAcidez < cateMateria:
            categoriaDefinitiva = cateAcidez
        else:
            categoriaDefinitiva = cateMateria

    return categoriaDefinitiva


def matrizAcidez(numeroDeZonas):
    mAcidez = []
    i = 0
    while i < numeroDeZonas:
        fila = input().split()
        for j in range(len(fila)):
            fila[j] = float(fila[j])
        mAcidez.append(fila)
        i += 1

    return mAcidez
    # llenar una sola funcion para crear matrices


def matrizMateria(numeroDeZonas):
    mMateria = []
    i = 0
    while i < numeroDeZonas:
        fila = input().split()
        for j in range(len(fila)):
            fila[j] = float(fila[j])
        mMateria.append(fila)
        i += 1

    return mMateria


def masYmenosRepeticiones(listaCategorias):
    c1, c2, c3, c4 = 0, 0, 0, 0
    for k in listaCategorias:
        if k == 0:
            c1 += 1
        elif k == 1:
            c2 += 1
        elif k == 2:
            c3 += 1
        elif k == 3:
            c4 += 1
    categorias = [c1, c2, c3, c4]
    # las categorias son los indice en donde
    # 0 es no apto
    # 1 es marginalmente apto
    # 2 es moderadamente apto
    # 3 es sumamente apto
    maximo = max(categorias)
    min = minimo(categorias)
    for index in range(len(categorias)):
        if categorias[index] == maximo:
            masRepite = index
        if categorias[index] == min:
            menosRepite = index

    # retorna las categorias que mas y menos se repiten
    return masRepite, menosRepite

# funcion para obtener el valor minimo sin tener en cuenta el cero


def minimo(lista):
    minimo = lista[0]
    for indice in range(1, len(lista)):
        if minimo > lista[indice] and lista[indice] != 0:
            minimo = lista[indice]
    return minimo


def main():
    if __name__ == "__main__":
        # contadores generales para categoria resultante
        cont1, cont2, cont3, cont4 = 0, 0, 0, 0
        numeroZonas = int(input())
        ma = matrizAcidez(numeroZonas)
        mm = matrizMateria(numeroZonas)
        salidaMasRepetidos = []
        salidaMenosRepetidos = []
        for zona in range(numeroZonas):
            listaDeCategorias = []
            for dia in range(7):
                # se selecciona la categoria de la acidez
                catAcidez = categoriaAcidez(ma[zona][dia])
                # se selecciona la categoria de la materia
                catMateria = categoriaMateria(mm[zona][dia])
                # se selecciona la categoria resultante
                resultante = categoriaResultante(catAcidez, catMateria)
                # lista de cateogira resultante
                listaDeCategorias.append(resultante)

                # conteo general por categorias
                if resultante == 3:
                    cont1 += 1
                elif resultante == 2:
                    cont2 += 1
                elif resultante == 1:
                    cont3 += 1
                elif resultante == 0:
                    cont4 += 1
            # las categorias que mas y menos se repiten por zona 
            masRepetido, menosRepetido = masYmenosRepeticiones(
                listaDeCategorias)

            if masRepetido == 0:
                salidaMasRepetidos.append("no apto")
            elif masRepetido == 1:
                salidaMasRepetidos.append("marginalmente apto")
            elif masRepetido == 2:
                salidaMasRepetidos.append("moderadamente apto")
            elif masRepetido == 3:
                salidaMasRepetidos.append("sumamente apto")

            if menosRepetido == 0:
                salidaMenosRepetidos.append("no apto")
            elif menosRepetido == 1:
                salidaMenosRepetidos.append("marginalmente apto")
            elif menosRepetido == 2:
                salidaMenosRepetidos.append("moderadamente apto")
            elif menosRepetido == 3:
                salidaMenosRepetidos.append("sumamente apto")

        print(cont4, cont3, cont2, cont1)
        print(",".join(salidaMasRepetidos))
        print(",".join(salidaMenosRepetidos))


main()
