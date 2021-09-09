try:
    file = open('text.txt', 'w')
    file.write('Add information to file\n')
    file.write('Goodbye')
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    file.close()