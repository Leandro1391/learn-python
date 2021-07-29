while True:
    number = int(input("Como estuvo tu dia (1 al 10)?: "))
    if not (number >= 1 and number <= 10):
        print("Error, Reingrese un numero del 1 al 10")
    else:
        print("Mi dia estuvo de", number)
        break

# print("Mi dia estuvo de", number)

# print("Mi dia estuvo de:", int(input("Como estuvo tu dia (1 al 10): ")))