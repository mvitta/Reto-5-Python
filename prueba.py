# contadores = [[30, 33, 30, 30], ["mari", "jean", "alej", "meke"]]

# # mostrando primer resultado sin ordenar
# print("*" * 10 + "Tabla" + "*" * 10)
# for col in range(len(contadores[0])):
#     print(contadores[1][col], contadores[0][col])

# # Aplicando METODO BURBUJA para ordenar las filas de contadores
# # y las filas de categorias
# # teniendo en cuenta los valores
# for i in range(len(contadores[0])):
#     for j in range(len(contadores[0]) - 1):
#         if contadores[0][j + 1] > contadores[0][j]:

#             aux = contadores[0][j + 1]
#             temp = contadores[1][j + 1]

#             contadores[0][j + 1] = contadores[0][j]
#             contadores[1][j + 1] = contadores[1][j]

#             contadores[0][j] = aux
#             contadores[1][j] = temp
#         elif contadores[0][j + 1] == contadores[0][j]:
#             # se evalua las categorias
#             if contadores[1][j] > contadores[1][j + 1]:
#                 auxCategoria = contadores[1][j]
#                 contadores[1][j] = contadores[1][j + 1]
#                 contadores[1][j + 1] = auxCategoria

# # mostrando resultado ordenado
# print("*" * 10 + "Tabla Ordenada Por Valores" + "*" * 10)
# for col in range(len(contadores[0])):
#     print(contadores[1][col], contadores[0][col])
# print()

# nombres = ["mori", "maik"]
# print(nombres[0] > nombres[1])
# print("no ordenado: ", nombres)
# if nombres[0] > nombres[1]:
#     temporal = nombres[0]
#     nombres[0] = nombres[1]
#     nombres[1] = temp
# print("ordenado: ", nombres)
# print("ordenado por metodo sorted: ", sorted(nombres))

arc = open("data.txt")

