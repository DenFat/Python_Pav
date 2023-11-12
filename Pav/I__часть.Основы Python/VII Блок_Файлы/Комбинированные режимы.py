# filename = 'example.txt'
#
# with open(filename, 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
#     for index, line in enumerate(lines):
#         if line.strip():
#             print(f'{index}: {line.strip()}')
#         else:
#             print(f'Строка {index}: пусто')

# s = 'Привет, как дела?'
# words = s.split()
#
# del words[0]
# joned_s = ' '.join(words)
#
# print(words)
# print(joned_s)

# s = 'Привет, как дела?'
# words = s.split(',')
#
# print(words)
#
# first_word = words[0]
# mod_word = first_word[:2] + 'e'+ first_word[3:]
# words[0] = mod_word
# print(words)
#
# mod_s = ','.join(words)
# print(mod_s)

# with open('example.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         word = line.split()
#         if int(word[1]) < 20:
#             line_s = line.strip()
#             print(line_s)

# with open('example1.txt', 'w+', encoding='utf-8') as file:
#     # Запись данных
#     file.write('Привет, мир\n')
#     file.write('Это пример данного режима w+')
#
#     file.seek(0)
#     # Чтение данных
#     data = file.read()

# with open('data.txt', 'a+', encoding='utf-8') as file:
#     # Запись данных
#     file.write('Привет, мир\n')
#
#
#     file.seek(0)
#     # Чтение данных
#
#     file.write('Это пример данного режима a+')
#     file.seek(0)
#     data = file.read()
#     print(data)

with open('data.txt', 'r+', encoding='cp1251') as file:
    # Запись первичных данных
    file.write('Старые данные\n')

    file.seek(0)
    data=file.read()
    print('Исходные дынные')
    print(data + '\n')
    # Запись вторичных данных
    # Перемещение указателя в начало файла для записи

    file.seek(0)

    file.write('Новые данные')
    file.seek(0)
    up_data = file.read()
    print('Обновленные данные')
    print(up_data)