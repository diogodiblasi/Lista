def soma_subsequente(lista):
    if len(lista) == 0:
        return 0

    maior_soma = 0
    soma_atual = 0

    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1] > 0:
            soma_atual += lista[i - 1]
        else:
            soma_atual += lista[i - 1]
            if soma_atual > maior_soma:
                maior_soma = soma_atual
            soma_atual = 0
    if maior_soma > 0:
        return maior_soma
    else:
        return max(lista)


lista1 = [1, 2, 3, 2]
lista2 = [1, 2, 2, 3, 2]
lista3 = [-1, 1, 6, -5]
lista4 = [2, 5, 1, 2, 5, 8, -1, 10, -2, 3]
lista5 = [9, 6, -1, -3, 10, -8, -6, 7, -9, 7]

print("Lista 1:", soma_subsequente(lista1))
print("Lista 2:", soma_subsequente(lista2))
print("Lista 3:", soma_subsequente(lista3))
print("Lista 4:", soma_subsequente(lista4))
print("Lista 5:", soma_subsequente(lista5))
