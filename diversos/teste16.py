teste = [0,1,2,3,4,5]
#teste.append([6,7])
teste.extend([6,7])

print(teste)

'''
lista = []
for i in range(11):
    lista.insert(i, i)

print(lista)
lista.pop([2,3])
print(lista)
'''
lista = list(range(11))  # Maneira mais eficiente de criar a lista

print(lista)  # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista = [x for x in lista if x not in (2, 3)]

print(lista)  # Saída: [0, 1, 4, 5, 6, 7, 8, 9, 10]
