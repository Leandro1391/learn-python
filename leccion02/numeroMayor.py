number1 = int(input('Ingresar primer numero: '))
number2 = int(input('Ingresar el segundo numero: '))

if (number1 > number2):
    print(f'El numero mayor es: {number1}')
elif (number1 < number2):
    print(f'El numero mayor es: {number2}')
else:
    print('No se puede distinguir cual es el mayor')