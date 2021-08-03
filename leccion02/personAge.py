age = int(input(f'Input your age: '))


if (age >= 20 and age < 30) or (age >= 30 and age < 40):
    print(f'Dentro de rango (20\'s) o (30\'s)')
    # if (age >= 20 and age < 30):
    #     print('Dentro de los 20\'s')
    # elif (age >= 30 and age < 40):
    #     print('Dentro de los 30\'s')
    # else:
    #     print('Out of range')
else:
    print('No está dentro de los 20\'s ni 30\'s')