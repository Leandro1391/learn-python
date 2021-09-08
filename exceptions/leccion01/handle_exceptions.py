try:
    10/0
except Exception as e:
    print(f'Handlde error: {e}')


# ZeroDivisionZero es una exception hija de Exception y este último es hija de BaseException