# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# if num1 > num2:
#     print(f'Первое число {num1} больше {num2}')
# if num1 == num2:
#     print(f'Первое число {num1} равно {num2}')
# else:
#     print(f'Второе число {num2} больше {num1}')

# num1 = int(input())
# if num1 % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# password = input('Введите пароль: ')
# if  password == 'qwerty':
#     print('Пароль принят')
# else:
#     print('Пароль неверный')

# name1 = 'Маша'
# name2 = 'Марк'
# if name1 > name2:
#     print(f'{name1} больше {name2}')
# else:
#     print(f'{name2} больше {name1}')

# Домашнее задание

# num = int(input('Введите число '))
# if num % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# password = input('Ввкдите пароль: ')
# pas = ['admin', 'uper', 'asdf']
# if password in pas:
#     print('Доступ разрешен')
# else:
#     print('ALLARM! ')
#     print('we called the police')

# num = int(input('Введите число: '))
# if  num > 0:
#     print('Введенное пользоватетелм число больше 0')
# elif num < 0:
#     print('Введенное пользоватетелм число меньше 0')
# else:
#     print('Введенное пользоватетелм число равно 0')

# num1 = 0
# ans = input('Введите значение: ')
# if ans == 'end':
#     num = 5
# elif ans == '10':
#     num = 6
# print(num)

# sub1 = int(input('Введите оценку по первому предмету: '))
# sub2 = int(input('Введите оценку по второму предмету: '))
# sub3 = int(input('Введите оценку по третьему предмету: '))
# average = (sub1 + sub2 + sub3)/3
# if average > 4.5:
#     print(f'Твой средний бал равен {"%.1f" % average}, молодец так держать!')
# elif 3 < average < 4.5:
#     print(f'Твой средний бал равен {"%.1f" % average}, надо подтянуть учебу!')
# else:
#     print(f'Твой средний ба3л равен {"%.1f" % average}, ЭТО ОЧЕНЬ ПЛОХО!')

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# if num1 > num2 and num1 > num3:
#     print(f'{num1} - максимальное число')
# elif num2 > num1 and num2 > num3:
#     print(f'{num2} - максимальное число')
# else:
#     print(f'{num3} - максимальное число')

# schoolboy = int(input('Введите количество школьников: '))
# apples = int(input('Введите количество яблок: '))
# div = apples // schoolboy
# remain = apples % schoolboy
# print(f'''Каждому школьнику достанется по {div} яблок.
# В корзинке останется - {remain} яблок''')

# salary = int(input('Введите заработную плату сотрудника за час работы: '))
# norma = int(input('Введите норму часов: '))
# coefficient = float(input('Введите коэфициент сверхурочного времени: '))
# job = int(input('Введите количество часов которые проработал сотрудник: '))
# if job > norma:
#     print(f'Повышенная зарабатная плата сотрудника равна {int(job * salary * coefficient)} рублей')
# else:
#     print(f'Стандартная зарплата сотрудника приработе {job} часов равна {salary * job} рублей')