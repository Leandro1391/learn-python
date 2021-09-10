try:
    file = open('test.txt', 'w', encoding='utf8')
    file.write('Add information to file\n')
    file.write('Goodbye - é')
except Exception as e:
    print(f'Exception - Error handled: {e}, {type(e)}')
finally:
    file.close()
    print(f'File ends')