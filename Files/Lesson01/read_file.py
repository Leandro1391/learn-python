try:
    file = open('test.txt', 'r', encoding='utf8')
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')

# Lee todos el contenido
# print(f'{file.read()}')

# Para leer hasta cierta cantidad de caracteres se debe comentar el print(f'{file.read()}') y luego lo siguiente
# print(f'{file.read(7)}')

# Lineas comletas
print(file.readline())
print(file.readline())

# w+:  escribir y leer informacion
# r+: abre lee y escribi el archivo