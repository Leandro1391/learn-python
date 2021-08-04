month = int(input('Ingrese mes del año (1-12) '))

# None es equivalente a null en otros lenguajes de programación como Java
season = None

if month >= 1 and month <= 3:
    season = 'Summer'
elif (month >= 4 and month <= 6):
    season = 'Autumn'
elif (month >= 7 and month <= 9):
    season = 'Winter'
elif (month >= 10 and month <= 12):
    season = 'Spring'
else:
    print('El valor ingresado no corresponde a un mes del año')

if season:
    print(f'La estacion es: {season}')