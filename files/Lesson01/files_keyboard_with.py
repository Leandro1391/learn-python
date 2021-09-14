from HandleFiles import HandleFiles

# el with es un Contexto Manager, se encarga de abrir y cerrar el arhicvo automaticamente
# with open('test.txt', 'r', encoding='utf8') as file:
#     print(file.read())


# with tiene dos metodos __enter__ que se encarga de abrir y __exit__ de cerrarlo, también lo podemos sobrescribir los metodos


with HandleFiles('test.txt') as file:
    print(file.read())