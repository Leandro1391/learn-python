# while True:
#     typeConvertion = input('Conversion de celsius a farenheit ingrese \'f\' o viceversa ingrese \'c\' ')
#     if typeConvertion == 'f':
#         temperature = float(input('Ingrese temperatura en celsius '))
#         print(f'En farenheit es {temperature * 9/5 + 32}')
#         break
#     elif typeConvertion == 'c':
#         temperature = float(input('Ingrese temperatura en farenheit '))
#         print(f'En celsius es {(temperature - 32) * 5/9 }')
#         break
#     else:
#         print(f'Ingreso un caracter incorrecto, por favor reingrese valor')



# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
        return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
        return (fahrenheit-32) * 5/9

# Realizamos algunas pruebas de conversión
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Los dos puntos después de la variable de resultado dan un formato de 2 digitos flotantes
print(f'{celsius} C a F: {resultado:.2f}')
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.2f}')
    