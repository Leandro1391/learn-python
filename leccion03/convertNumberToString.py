number = int(input('Ingrese un valor entre 1 y 3: '))
numberText = ''

if number == 1:
    numberText = 'Número uno'
elif number == 2:
    numberText = 'Número dos'
elif number == 3:
    numberText = 'Número tres'
else:
    numberText = 'Valor fuera de rango'
print(f'Numero ingresado: {number} - {numberText}')