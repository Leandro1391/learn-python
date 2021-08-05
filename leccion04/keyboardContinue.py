# for i in range(6):
#     if i % 2 == 0:
#         print(f'Value: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Value: {i}')

# La palabra continue ejecuta la siguiente iteración y no las lineas que sigue