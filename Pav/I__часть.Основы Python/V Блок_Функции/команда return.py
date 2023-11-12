# def count_toys():
#     return 10
#
#
# # print(count_toys())
# num = count_toys()
# # print(num)
#
# # if count_toys() > 9:
# if num > 9:
#     print('Еще рано заказыватьть новые игрушки')
# else:
#     print('Пора заказывать новые игрушки')

# def summa(x,y):
#     return x + y
#
#
# print(summa(5,10))


# def get_user_input():
#     user_name = input('Введите имя: ')
#     return user_name
#
#
# def greet_user():
#     return f'Привет, {get_user_input()}'
#
#
# def main():
#     print(greet_user())


# def get_user_input():
#     user_name = input('Введите имя: ')
#     return user_name
#
#
# def greet_user(name):
#     return f'Привет, {get_user_input()}'
#
#
# def main():
#     get_user_input()


# def get_student_grades():
#     math = int(input('Введите  оценку по математике: '))
#     physics = int(input('Введите  оценку по физике: '))
#     history = int(input('Введите  оценку по истории: '))
#     return math, physics, history
#
#
# def calculate_average(math, physics, history):
#     return (math + physics + history) / 3
#
# def print_report(calc):
#     return f'Средний бал студента {calc:.2f}'
#
# def main():
#     math, physics, history = get_student_grades()
#     calc = calculate_average(math, physics, history)
#     print(print_report(calc))
#
# main()

# def shop(your_money=1500):
#     sell_1 = int(input('Первая покупка: '))
#     sell_2 = int(input('Вторая покупка: '))
#     return your_money - (sell_1 + sell_2)
#
# print(shop(1000))
# print(shop())

# def foo(a):
#     if a % 2 == 0:
#         rez = "Введенное число четное"
#     else:
#         rez = "Введенное число нечетное"
#     return rez
# print(foo(2))

# def foo(a,b):
#     print(f"Первое введенное число: {a}")
#     print(f"Второе введенное число: {b}")
#     return a + b
#
# print(f"Сумма веденных числе равна {foo(3,4)}")

# def gret(name):
#     return f"Приветствую Вас {name}!"
#
#
# def main():
#     name =input("Введите своё имя: ")
#     print(gret(name))
#
#
# main()

def calc(price,quantity):
    return f"Общая стоимость товара равна: {price*quantity}"
price = int(input("Введите стоимость единицы товара: "))
quantity = int(input("Введите количиество товара на складе: "))
print(calc(price, quantity))