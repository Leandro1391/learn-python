try:
    file = open('test.txt', 'r', encoding='utf8')
    print(type(file))
    
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')

# Lee todos el contenido
# print(f'{file.read()}')

# Para leer hasta cierta cantidad de caracteres se debe comentar el print(f'{file.read()}') y luego lo siguiente
# print(f'{file.read(7)}')

# Lineas comletas
# print(file.readline())
# print(file.readline())

# r: Read - Default value. Opens a file for reading, error if the file does not exist
# a: Append - Opens a file for appending, creates the file if it does not exist
# w: Write: Opens a file for writing, creates the file if it does not exist
# x: Create: Creates the specified file, return an error if the file exist

# w+:  escribir y leer informacion
# r+: abre lee y escribe el archivo


# loop lines in the file
# for line in file:
#     print(line)

# Read lines - return a list
# print(file.readlines())

# access one line in the list
# print(file.readlines()[2])

# opened a new file
# a - anexa infromacion
file2 = open('copy.txt', 'a', encoding='utf8')
file2.write(file.read())

file.close()
file2.close()
print('It has ended all the process information')


