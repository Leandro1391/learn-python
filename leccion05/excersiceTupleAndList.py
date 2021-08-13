tupla = (13, 1, 8, 2, 3, 25, 8)
listNumbers = []

for lista in list(tupla):
    if lista < 5:
        listNumbers.append(lista)

print(listNumbers)