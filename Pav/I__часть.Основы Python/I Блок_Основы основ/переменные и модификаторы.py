# number = 1
# print(number + 10 > 15)
# print('number')

# message = 'Привет!'
# print(message + ' Я - программа')

# text = input('Представьтесь пожалуйста: ')
# print(text)

# num = 2
# num2 = 10
# summa = num + num2
# print(summa)

# num = 1
# print(num)
# num = 'Два'
# print(num)
# num = 3
# print(num)

# a, b, c = 3, 4, 1
# print(a, b, c)

# d = 50
# g = 20
# m = 5
# w = 15
# print(f'У Васи было {d} яблок, {g} ежиков, {m} бананов, {w} лимонов')

# print(type('Князь'))
# print(type(16))
# print(type(16.3))

# num1 = int(input('Первое число '))
# num2 = int(input('Второе число '))
# result = num1 + num2
# print(result)

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# print(f'Сумма двух чисел {num1} + {num2} = {num1 + num2}')
# print(f'Разность двух чисел {num1} - {num2} = {num1 - num2}')
# print(f'Произведение двух чисел {num1} * {num2} = {num1 * num2}')
# print(f'Частное двух чисел {num1} / {num2} = {num1 / num2}')
# print(f'Степень числа {num1} на {num2} = {num1 ** num2}')

# number1 = 123
# number2 = 7.8
# str_ = 'string'
# print(f'{number1} {number2} {str_}')

# age = int(input('Введите ваш возраст: '))
# print(f'Ваш возраст через два года будет: {age + 2}')

# ogr = int(input('Укажите длинну ограды: '))
# sec = int(input('Укажите длину секции: '))
# print(f'''При длине секции в {sec} метров, количество секций будет равно: {ogr // sec}
# Остаток материалла будет равен: {ogr % sec} метров.''')

# money = int(input('Введите количество денег: '))
# cost = int(input('Введите стоимость детали: '))
# print(f'На сумму {money} рублей, вы можете купить: {money // cost} деталей. У вас останется {money % cost} рублей')

# first_name = input('Введите ваше имя: ')
# last_name = input('Введите вашу фамилию: ')
# full_name = first_name + ' ' + last_name
# print(f'Приветствую {full_name}')

# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# c = int(input('Введите третье число'))
# f = (((a * b) + (a * c)) ** 3) / 2
# print(f'Искомое число: {f}')

# first_name = input('Введите имя: ')
# surname = input('Введите отчетсво: ')
# last_name = input('Введите фамилию: ')
# data_age = input('Введите дату рождения: ')
# place_of_birth = input('Введите место рождения: ')
# job = input('Введите место работы или учебы: ')
#
# print(f'''ИМЯ: {first_name}\nОТЧЕСТВО: {surname}
# ФАМИЛИЯ: {last_name}\n{'*' * 9}\nДата рождения: {data_age}
# Место рождения: {place_of_birth}\nМесто работы или учебы: {job}
# {'*' * 9}''')

# aples = int(input('Введите количество собраных яблок: '))
# student = int(input('Введите количество учеников: '))
# print(f'Ученикам досталось по {aples // student} яблок. В корзине осталось {aples % student} яблок')

# first_name = input('Введите ваше имя: ')
# age = int(input('Введите ваш возраст: '))
# place = input('Введите место проживания: ')
# country = input('Введите страну проживания: ')
# print(f'Уважаемый {first_name}! На сегодняшний день\n Вы проживаете '
#       f'в стране {country}, в\n городе {place} и вы\n'
#       f' роделись в {2023 - age}году.')

# num = int(input('Введите число: '))
# print(f'Вы ввели {num}. Предыдущее число - {num - 1}.'
#       f'Последующее число - {num + 1}')

# start = int(input('Введите количество секунд: '))
# min = start // 60
# sec = start % 60
# print(f'С момента запуска прошло {min} минут и {sec} секунд')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# print(f'''{num1} * {num2} = {num1 * num2}
# {num1} / {num2} = {num1 / num2}
# {num1} + {num2} = {num1 + num2}
# {num1} - {num2} = {num1 - num2}''')

# apples  = int(input('Введите количество яблок: '))
# bananas = int(input('Введите количество бананов: '))
# apples_boxes = apples // 10
# apples_units = apples % 10
# bananas_packages = bananas // 6
# bananas_units = bananas % 6
# print(f''' Вы должны купить {apples_boxes} ящиков яблок и
# {apples_units} штук отдельно и {bananas_packages} пакетов бананов и
# {bananas_units} в добавок''')

# pen = int(input('Укажите цену ручки в копейках: '))
# rub = int(input('Введите количество рублей: '))
# cop = int(input('Введите количество копеек: '))
# summa = (rub * 100) + cop
# print(f'При стоимости ручки {pen} копеек, можно купить {summa // pen} ручек')
