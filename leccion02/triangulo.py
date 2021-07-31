while True:
    try:
        altura = int(input('Ingresar altura del triangulo: '))
        base = int(input('Ingresar base del triangulo: '))
        if not (altura > 0 and base > 0):
            print(f'Los parametros ingresados deben ser mayor a 0')
        else:
            break
    except Exception as e:
        print(f'Error al ingresar un parametro que no pertenece a los enteros, por favor ingrese un numero entero')

print(f'Area: {base * altura}')
print(f'Perímetro: {(base + altura)*2}')