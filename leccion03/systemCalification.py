calificationNumber = int(input('input calification '))
note = None

if 0 <= calificationNumber < 6:
    note = 'F'
elif 6 <= calificationNumber < 7:
    note = 'D'
elif 7 <= calificationNumber < 8:
    note = 'C'
elif 8 <= calificationNumber < 9:
    note = 'B'
elif 9 <= calificationNumber <= 10:
    note = 'A'
else:
    print('Incorrect calification value')

if note:
    print(f'La nota es: {note}')