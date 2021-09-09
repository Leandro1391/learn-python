result = None
# a = 10
a = '10'
b = 0

try:
    result = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Error handled: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Error handled: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')


print(f'Resultado: {result}')
print(f'Continue....')


# ZeroDivisionZero es una clase exception hija de Exception y este último es hija de BaseException que es el padre de todas las excepciones