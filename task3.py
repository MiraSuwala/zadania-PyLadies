# Napisz funkcję delta_compression, która jako argument
# przyjmuje posortowaną listę liczb całkowitych
# i zwróci tę samą listę skompresowaną następującym algorytmem:
#   *Pierwszy element listy wyjściowej jest taki sam jak pierwszy element listy wejściowej.
#   *Każdy następny element listy wyjściowej jest równy różnicy
#    między odpowiadającym mu elementem listy wejściowej a elementem poprzedzającym go

lista_wejsciowa_we_1 = [5, 7, 11, 21, 28, 39]


def delta_compression(lista_wejsciowa_we):
    n = len(lista_wejsciowa_we)
    lista_wyjsciowa_wy = [lista_wejsciowa_we[0]]
    for i in range(1, n):
        lista_wyjsciowa_wy.append(lista_wejsciowa_we[i] - lista_wejsciowa_we[i - 1])
    print(lista_wyjsciowa_wy)


delta_compression(lista_wejsciowa_we_1)

input('\nPress enter to exit')

