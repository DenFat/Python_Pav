# Логический оператор end
#
# print(10 > 0 and 5 > 0)  # Вернет True
# print(10 % 2 == 0 and 12 % 2 == 0)  # Вернет True
# print('ма' in 'мама мыла раму' and 5 > 0)  # Вернет True
#
# print(10 > 0 and 5 > 0)  # Вернет True
# print(10 % 2 == 0 and 12 % 2 == 0)  # Вернет True
# print('ма' in 'мама мыла раму' and 5 > 0)  # Вернет True

# day = 3
# if (day >= 0) and (day <= 5):
#     print('Число входит в диапазон')

# python  = 'питон'
# coffe = 'кофе'
# cat = 'кот'
#
# # result = len(python) < 5 and len(coffe) and len(cat) < 5
# result = len(python) < 5 or len(coffe) < 5 or len(cat) < 5
# print(result)

# a = int(input())
# b = 4
# c = 3
# v = a > b or b == 2
# print(v)

# Логический оператор not
# print(not False)

# x = 0
# if not x:
#     print('x не равно нулю')
# else:
#     print('x равно нулю')

# my_string = ''
# if not my_string:
#     print('Строка пустая')
# else:
#     print('Строка не пустая')

# a = int(input())
# b = int(input())
#
# c = a * b
# if c % 2 == 0 or \
#     c % 3 == 0 or \
#     c % 4 == 0 or \
#     c % 5 == 0:
#
#     print('Произведение кратно 2 или 3 или 4 или 5')


# day = int(input('Введите номер дня недели: '))
# if day == 1:
#     print('''Гардероб:
#     * Почистить и убрать несезонные вещи
#     * Выбросить старые ненужные вещи
#     * Протереть шкаф и полки от пыли
#     * Разместить сезонные вещи, обувь аксесуары''')
# elif day == 2:
#     print('''Шкаф:
#     * Разобрать предметы
#     * Выкинуть ненужное
#     * Протереть от пыли полки''')
# else:
#     print('Отдыхать :)')

# num = int(input('Введите число от 1 до 10: '))
# if num == 1:
#     print('I')
# elif num == 2:
#     print('II')
# elif num == 3:
#     print('III')
# elif num == 4:
#     print('IV')
# elif num == 5:
#     print('V')
# elif num == 6:
#     print('VI')
# elif num == 7:
#     print('VII')
# elif num == 8:
#     print('VIII')
# elif num == 9:
#     print('IX')
# elif num == 10:
#     print('X')
# else:
#     print('ОШИБКА! Число должно быть в диапазоне от 1 до 10')

# age = int(input('Введите возраст человека: '))
# sex = input('Введите пол м/ж: ')
# if age <= 1:
#     print('Младенец')
# elif 1 < age < 13:
#     print('Подросток')
# elif age >= 13 and age < 20 and sex.lower() == 'м':
#     print('Юноша')
# elif age >= 13 and age < 20 and sex.lower() == 'ж':
#     print('Девушка')
# else:
#     print('Взрослый')

# num = int(input('Введите число: '))
# if num == 0:
#     print('Введенное число равно 0')
# elif num % 2 == 0:
#     print(f'Введенное число {num} является четным')
# else:
#     print(f'Введенное число {num} является нечетным')

# weight = int(input('Введите ваш вес: '))
# if weight >= 20 and weight <= 40:
#     print('Вам не мешало бы просто поесть')
# elif weight >= 41 and weight <= 60:
#     print('Остановись мгновенье  и пойдем качаться')
# elif weight >= 61 and weight <= 90:
#     print('Еще снаряд и нам конец!!!')
# elif weight >= 110 and weight <= 150:
#     print('Еда ? Забудь о этом слове')
# elif weight <= 20 or weight >= 200:
#     print('Дети и мутанты не обслуживаются!')
# else:
#     print('Измените значение веса')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# if num1 > num2:
#     print(f'{num1} больше {num2}')
# elif num2 > num1:
#     print(f'{num2} больше {num1}')
# else:
#     print('Числа равны')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# if num1 > num2:
#     print(f'число {num1} большее из введенных')
# elif num2 > num1:
#     print(f'число {num2} большее из введенных')
# else:
#     print('Числа равны')

# num = int(input('Введите число: '))
# if num % 5 == 0:
#     print('Вы выйграли')
# elif num % 10 == 0:
#     print('Вы проиграли')
# elif num % 2 == 0:
#     print('Сыграйте еще раз')

# long1 = int(input('Введите длинну первого прямоугольника: '))
# width1 = int(input('Введите ширину первого прямоугольника: '))
# long2 = int(input('Введите длинну второго прямоугольника: '))
# width2 = int(input('Введите ширину второго прямоугольника: '))
# square1 = long1 * width1
# square2 = long2 * width2
# if square1 > square2:
#     print(f'Площадь {square1} первого прямоугольника больше площади '
#           f'{square2} второго прямоугольника')
# elif square2 > square1:
#     print(f'Площадь {square2} второго прямоугольника больше площади '
#           f'{square1} первого прямоугольника')
# else:
#     print(f'Прямоугольники равны и их площадь составляет {square1}')

# num = int(input('Введите число: '))
# if num % 3 == 0 and num % 7 == 0:
#     print(f'Число {num} делится на 3 и на 7 без остатка')
# else:
#     print('Введите другое число')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# if num1 > num2 and num1 > num3:
#     print(f'Число {num1} большее из введенных')
# elif num2 > num3 and num2 > num1:
#     print(f'Число {num2} большее из введенных')
# elif num1 == num2 and num1 == num3:
#     print('Числа равны')
# else:
#     print(f'Число {num3} большее из введенных')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# if num1 < 0 and num2 < 0:
#     print(f'Числа {num1} и {num2} являются отрицательными')
# elif num1 > 0 and num2 > 0:
#     print(f'Числа {num1} и {num2} являются положительными')
# elif num1 == 0 and num2 == 0:
#     print(f'Числа {num1} и {num2} равны нулю')
# elif (num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0):
#     print(f'Числа {num1} и {num2} имеют разные знаки')

# num = int(input('Введите число: '))
# if num >= 0 and num <= 150 and not(num %2 == 1) and num > 70 and num < 140:
#     print('Число соответствует требованиям')
# else:
#     print('Выберем другое число')

# coin5 = int(input('Введите количество монет номиналом 5 копеек: '))
# coin10 = int(input('Введите количество монет номиналом 10 копеек: '))
# coin50 = int(input('Введите количество монет номиналом 50 копеек: '))
# rezult = 0
# if coin5 >= 0:
#     rezult += coin5 * 5
# if coin10 >= 0:
#     rezult += coin10 * 10
# if coin50 >= 0:
#     rezult += coin50 * 50
# if rezult == 100:
#     print('Поздарвляю сумма ваших монет равна рублю')
# elif rezult < 100:
#     print(f'Сумма монет {rezult} копеек и это менее одного рубля')
# elif rezult > 100:
#     print(f'Сумма монет {rezult} копеек и это более одного рубля')

# weight = int(input('Введите массу тела человека в килограммах: '))
# height = float(input('Введите рост человека в метрах: '))
# itm = weight/height ** 2
# if itm >= 18.5 and itm <= 25:
#     print(f'Индекс массы тела равен {round(itm, 1)} и он оптимален')
# elif itm <  18.5:
#     print(f'Индекс массы тела равен {round(itm, 1)} и он ниже нормы')
# else:
#     print(f'Индекс массы тела равен {round(itm, 1)} и он выше нормы')

# print('Приветствую! Я робот-кассир и буду сегодня Вас обслуживать')
# print('Для оформления вашего билета, мне необходимо занести в него некоторые данные')
# print('Прошу заполнить анкету, представленную ниже')
# name = input('Введите Ваше имя: ')
# height = float(input('Введите Ваш рост в метрах: '))
# weight = int(input('Введите Ваш вес в килограммах: ')
# print('Если вы хотите по полной оттянуться, прошу сообщите сколько у вас денег?')
# coin = int(input('Введите количество денег в рубях'))
# print()

# print('Привет, я твой личный помощьник - Мелиса')
# print('Для начала мне надо собрать необходимую инфомацию о тебе')
# print('Ответь на ряд вопросов ниже:')
# name = input('Введи своё имя: ')
# age = int(input(f'Олично {name}, рада знакомству. А сколько тебе лет? '))
# city = input(f'Ого {age}, да ты в самом рассвете сил {name}! А в каком городы ты проживаешь? ')
# choice = input('Ваш профиль создан! Хотите ли вы его посмотреть лил продолжим работу? (y/n) ')
# if choice.lower() == 'y':
#     print('*' * 20)
#     print(f'Имя - {name}\nВозраст - {age}\nГород - {city}')
#     print('*' * 20)
# else:
#     print(f'Отлично {name}, приступим к работе!')

