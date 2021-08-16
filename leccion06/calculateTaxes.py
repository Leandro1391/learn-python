pago_sin_impuesto = float(input(f'Ingresar monto: '))
impuesto = float(input(f'Ingresar porcentaje de impuesto: '))

def calcular_total(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto * ((impuesto/100) + 1)

print(f'El monto con impuesto es: {calcular_total(pago_sin_impuesto, impuesto)}')