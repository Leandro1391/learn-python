# def sumListNumbers(*numbers):
#     sum = 0
#     for number in numbers:
#         sum += number
#     print(f'The total is: {sum}')

# sumListNumbers(50, 100, 30, 1)

def sumListNumbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sumListNumbers(50, 100, 30, 1))

def productListNumbers(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total

print(productListNumbers(50, 100, 30, 1))

