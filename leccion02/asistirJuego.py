vacaciones = False
diaDescanso = True

if (vacaciones or diaDescanso):
    print(f'Puede asistir al juego de su hijo')
else:
    print(f'No puede asistir al juego de su hijo')

# With not
if not (vacaciones or diaDescanso):
    print(f'No puede asistir al juego de su hijo')
else:
    print(f'Puede asistir al juego de su hijo')