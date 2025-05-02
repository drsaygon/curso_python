import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2022))

# print(calendar.month(2022, 12)) 

# print(calendar.monthrange(2022, 12))

# print(list(enumerate(calendar.day_name)))

# for week in calendar.monthcalendar(2022, 12):
#     for day in week:
#         if day == 0:
#             continue
#         print(day)


# O Bubble Sort funciona comparando e trocando elementos adjacentes, repetidamente, até que a lista esteja ordenada

# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(n - 1):
#             if lista[j] > lista[j + 1]:
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#     return lista

# numeros = [5, 2, 9, 1, 5, 6]
# print(bubble_sort(numeros))  # Resultado ordenado


# Gerando a matriz do mês de dezembro de 2022
mes = calendar.monthcalendar(2022, 12)

# Criando uma lista com todos os dias válidos (removendo os zeros)
dias = [dia for semana in mes for dia in semana if dia != 0]

# Função Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ordenando os dias
dias_ordenados = bubble_sort(dias)

# Exibindo a lista ordenada
print(dias_ordenados)
