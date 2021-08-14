# Default parameters and with arrow we can indicate the posible type data to return
def sum(a:int = 0, b:int = 0) -> int:
    return a + b

# result = sum(5, 74)
# print(f'The result is {result}')

print(f'The result is {sum(70, 10)}')

# Also we can assign default values in the function parameters

# especificar los datos son redundantes en python porque es dinmaíco el comportamiento de la variables pero sirve par aindicar