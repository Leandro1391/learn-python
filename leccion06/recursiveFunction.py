# Funcion recursiva es como realizar el factorial de cinco 5!, es decir, consiste en llamar a si mismo la funcion

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

# result = factorial(6)
number = 6
print(f'The factorial of {number} is {factorial(number)}')