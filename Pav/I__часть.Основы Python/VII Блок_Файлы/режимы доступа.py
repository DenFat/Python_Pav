 # with open('пояснительная.txt', 'w', encoding='utf-8') as file:
    # file.write('Опаздал, потому что Игорь\n')  # Запись строки из метода
    # file.write('А Игорь - потому что так надо')  # Запись строки из метода

    #  Запись данных из итерируемой последовательности
    # file.writelines(['Опаздал, потому что Игорь\n','А Игорь - потому что так надо'])

    # if file.writable():  # доступен ли файл для записи
    #     file.write('Ура, мы записали данные')
    # else:
    #     print('Невозможно осуществить запись данных')

# with open('пояснительная.txt', 'a', encoding='utf-8') as file:
#     file.write('Я люблю Python \n')
#     file.write('Я люблю Программирование\n')

# with open('пояснительная.txt', 'w', encoding='utf-8') as file:
#     file.write('Первая строка\n')
#
# with open('пояснительная.txt', 'a', encoding='utf-8') as file:
#     file.write('Вторая строка')

# with open('Call_book.txt', 'r', encoding='utf-8') as file:
    # print(file.read())  # Чтение всего содержимого файла
    # con = file.read()  # Чтение всего содержимого файла

    # con = file.readline()  # Чтение одной строки

    # con = file.readlines()  # Чтение всех строк из файла. Возвращает список строк

    # for line in file:
    #     if 'Игорь' in line:
    #         print(line, end='')

# second_line = con[1]
#
# print(con)
# print(second_line)

# from random import randint
#
# with open('тест.txt','w', encoding='utf-8') as  file:
#     for i in range(10):
#         num = randint(0,20)
#         file.writelines([f'{num}\n'])
#         if i == 9:
#             file.writelines([f'{num}'])

with open('../../Файлы/тест.txt', 'r', encoding='utf-8') as  file:
    line_number = 1
    for i in file:
        if int(line_number) % 2 == 0:
            print(i.strip())
        line_number +=1