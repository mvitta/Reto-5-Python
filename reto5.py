def main():
    if __name__ == "__main__":
        ciudad = input()
        linea, sumaAcidez, sumaMateria = 0, 0, 0
        valoresAcidez, valoresMateria = [], []
        contNoApto, contMarginalmente, contModeradamente, contSumamente = 0, 0, 0, 0
        l = 0
        with open("data.csv", "r") as archivo:
            while l <= 100001:
                contenido = archivo.readline().split(",")
                if contenido[0] == ciudad:
                    # id_zona
                    contenido[1] = int(contenido[1])
                    # acidez
                    contenido[2] = float(contenido[2])
                    valoresAcidez.append(contenido[2])
                    sumaAcidez += contenido[2]
                    # materia organica
                    contenido[3] = float(contenido[3])
                    valoresMateria.append(contenido[3])
                    sumaMateria += contenido[3]
                    # p2o5
                    contenido[4] = int(contenido[4])
                    # ca
                    contenido[5] = float(contenido[5])
                    # aptitud
                    contenido[6] = contenido[6].rstrip("\n")
                    # conteo de categorias
                    if contenido[6] == "no apto":
                        contNoApto += 1
                    elif contenido[6] == "marginalmente apto":
                        contMarginalmente += 1
                    elif contenido[6] == "moderadamente apto":
                        contModeradamente += 1
                    elif contenido[6] == "sumamente apto":
                        contSumamente += 1

                    linea += 1

                l += 1
        contadores = [
            [contSumamente, contMarginalmente, contModeradamente, contNoApto, ],
            ["sumamente apto", "marginalmente apto",
                "moderadamente apto",  "no apto"]
        ]
        # metodo burbuja para ordenar
        for i in range(len(contadores[0])):
            for j in range(len(contadores[0]) - 1):
                # si son diferentes ordena de forma normal
                if contadores[0][j + 1] > contadores[0][j]:

                    aux = contadores[0][j + 1]
                    temp = contadores[1][j + 1]

               # maxt =     #[1, 2, 3, 4] max = 4 pos = 3
                    # [5, 4, 2, 3] maxt [1][pos]

                    contadores[0][j + 1] = contadores[0][j]
                    contadores[1][j + 1] = contadores[1][j]

                    contadores[0][j] = aux
                    contadores[1][j] = temp

                elif contadores[0][j + 1] == contadores[0][j]:
                    # si hay valores iguales ordena alfabeticamente las categorias
                    if contadores[1][j] > contadores[1][j + 1]:
                        auxCategoria = contadores[1][j]
                        contadores[1][j] = contadores[1][j + 1]
                        contadores[1][j + 1] = auxCategoria
        # SALIDAS
        print("{:.2f}".format(sumaAcidez / linea),
              "{:.2f}".format(sumaMateria / linea))
        print(min(valoresAcidez), min(valoresMateria))
        print(max(valoresAcidez), max(valoresMateria))
        for col in range(len(contadores[0])):
            print(contadores[1][col], contadores[0][col])


main()
