try:
    print('Proporcione los siguientes datos del libro:')
    name = input('Proporciona el nombre: ')
    id = int(input('Proprociona el ID: '))
    precio = float(input('Proporcione el precio: '))
    envio = input('Indica si el envio es gratuito (True/False): ')

    if envio == "True":
        envio = True
    elif envio == "False":
        envio = False
    else:
        envio = False
        # envio = 'Valor incorrecto escribir True o False'

    
    print(f'''
        Nombre: {name}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envio}
    ''')

    # print(f'Nombre: {name}')
    # print(f'Id: {id}')
    # print(f'Precio: {precio}')
    # print(f'Envio Gratuito?: {envio}')

except Exception as e:
    print(f'Handle Exception {e}')


# bool(input()) la clase bool solamente valida si la cadena es disinto de vacio es True en caso contrario Flase