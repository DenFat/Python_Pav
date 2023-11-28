# my_dict_1 = {}  # при помощи фигурных скобок
# my_dict_1['Имя'] = 'Игорь'
# my_dict_1['Возраст'] = 30
# print(my_dict_1)
#
# my_dict_2 = dict()  # при помощи функции dict()
# print(my_dict_2)
#
# keys = ['Игра', 'Age']
# values = ['Sims4', 30]
#
# my_dict_3 =dict(zip(keys,values))
# print(my_dict_3)

# my_dict = {
#     [1, 2]: 'списки не могут быть ключами',
#     1: 'целые числа могут быть ключами',
#     'строки': 'строки могут быть ключами',
#     8.6: 'вещественные числа',
#     True: 'логическое значние'
# }
# print(my_dict)

# my_dict = {
#     # ключи могут быть только уникальными
#     1: 'целые числа могут быть ключами',
#     True: 'логическое значние'
# }
# print(my_dict)

# d1 = {'b':2, 'a':1}
# d2 = {'a':1, 'b':2}
#
# # print(d1 == d2)
#
# # my_dict = {'hello': True}
# # print(my_dict[1:1])
#
# my_dict = dict()
# my_dict['россия'] = 'Москва'
# my_dict['белорусь'] = 'Минск'
# my_dict['франция'] = 'Париж'
# # print(my_dict)
# # print(my_dict['Россия'])
#
# answer = input('Введите название страны: ').lower()
# if answer in my_dict:
#     print(f' Страна {answer}, столица - {my_dict[answer]}')
# else:
#     print('Такой страны не найдено')
#     choice = input('Добавить новую страну? (да/нет)').lower()
#     if choice == 'да':
#         country = input(f'Введите столицу страны {answer}')
#         my_dict[answer] = country

# my_dict1 = {}
# my_dict1['Имя'] = 'Денис'
# my_dict1['Возраст'] = 44
# print(my_dict1)

# alien = {'color': 'green', 'points': 5}
# print(alien['color'])
# print(alien['points'])
#
# alien['color'] = 'white'
# alien['points'] = 10
#
# print(alien['color'])
# print(alien['points'])

# name = input('Введите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
# my_dict = {}
# my_dict['name'] = name
# my_dict['age'] = age
# print(f'Привет, {my_dict["name"]}! Тебе {my_dict["age"]} лет')

# str1=[]
# str2=[]
# string = input('Введите строку ').lower()
# for i in string:
#     str1.append(i)
# str1 = ' '.join(str1).split()
# str2 = str1[::-1]
# if str1 == str2:
#     print(f'Строка "{string}" - является палиндромом')
# else:
#     print(f'Строка "{string}" - НЕ является палиндромом')

# s = input('Введите строку: ')
# if s == s[::-1]:
#     print('Строка является палиндромом')
# else:
#     print('Строка не является палиндромом')

# Более интересный вариант:
# s = input('Введите строку: ')
# print('Строка является палиндромом' if s == s[::-1] else 'Строка не является палиндромом')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# choice = input('Выберите действие | + | - | * | / | ')
# dict_math = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2}
# print(f'число {num1} {choice} {num2} = {dict_math[choice]}')

# st1=[]
# def addElement():
#     while True:
#         num = input('Ввести элемент: ')
#         st1.append(num)
#         choice = input('Ввести еще один элемент? ( да / нет )').lower()
#         if choice == 'нет':
#             break
# def printElenent(str):
#     for i in str:
#         print(f'{i}\n')
# addElement()
# printElenent(st1)

# letter_count = {}
#
# word = input('Введите слово: ')
# for letter in word:
#     if letter == 'а':
#         if letter in letter_count:
#             letter_count[letter] += 1
#         else:
#             letter_count[letter] = 1
# if 'а' in letter_count:
#     print(f"В слове {word}, количество букв 'a' равно {letter_count['а']}")
# else:
#     print(f"В слове {word}, нет буквы 'a'.")

# word_dict = {}
# list = ['мама', 'мир', 'дом', 'мама']
# for word in list:
#     if word in word_dict:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1
# print(word_dict)

# list = ['3', '2', '4', '9', '12', '23']
# summ = 0
# for num in list:
#     summ += int(num)
# print(f"Среднее значение списка равно {summ/len(list)}")

# def squareNumDict(num):
#     numDict = {}
#     for i in range(1,num+1):
#         numDict[i] = i**2
#     return numDict
# print(squareNumDict(4))

# words = input('Введите список слов через запятую: ').split()
# longest_word = ''
# max_length = 0
# for word in words:
#     if len(word) > max_length:
#         longest_word = word
#         max_length = len(word)
# result = {longest_word: max_length}
# print(result)

# string = input('Введите строку: ').split()
# stringDict = {}
# for str in string:
#     if str in stringDict:
#         stringDict[str] += 1
#     else:
#         stringDict[str] = 1
# print(stringDict)