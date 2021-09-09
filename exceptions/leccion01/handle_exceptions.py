from NumbersEqualsException import NumbersEqualsException

result = None
# a = 10
# a = '10'
# b = 0

# RAISE: permite lanzar un exception | throw a exception

try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    if a == b:
        # This is a throw exception with raise - arroja cualquier tipo de exception puede ser un raise functinName()
        raise NumbersEqualsException('Numbers are equals')
    result = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Error handled: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Error handled: {e}, {type(e)}')
except ValueError as e:
    print(f'ValueError - Error handled: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
else:
    # este bloque no se va ejecutar si se arroja un error
    print(f'No throw exception')
finally:
    # este blque siempre se va a ejecutar - Sirve para liberar recursos, para avisar al usuario como termino el manejo de escepciones o cierre de archivos
    print(f'Ejecución del bloque finally')
    
    


print(f'Resultado: {result}')
print(f'Continue....')


# ZeroDivisionZero es una clase exception hija de Exception y este último es hija de BaseException que es el padre de todas las excepciones