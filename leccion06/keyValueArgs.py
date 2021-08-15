# Diccionario variables

def listTerms(**terminos):
    for key, value in terminos.items():
        print(f'{key}: {value}')

# the key hasn't double quotes and value can be any type of data
listTerms(IDE='Integrated Development Enviroment', PK='Primary Key')
listTerms(VS='Visual Code')

# también podemos pasar arguments fijos, una tupla de elementos variable y un diccionario variables
# def listTerms(name, *names,**terminos):
#     for key, value in terminos.items():
#         print(f'{key}: {value}')