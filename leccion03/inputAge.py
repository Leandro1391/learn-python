age = int(input('Input your Age: '))
message = None

# if (age >= 0 and age < 10):
if (0 <= age < 10):
    message = 'Incredible childhood'
elif (10 <= age < 20):
    message = 'A lot of changes and hard work study'
elif (20 <= age < 30):
    message = 'Love and start to work'
else:
    print('Chapter of life not recognise')

print(f'Your age is: {age}, {message}')