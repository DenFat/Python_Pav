# my_list = [1, 2, 3] # прямое создание
#
# my_list = []    # c помощью append
# for i in range(5):
#     my_list.append(i)
#
# my_list = [0]*5 # создание списка с помощью знака умножения
# print(my_list)
#
# my_s = 'Hello'  # с помощью split()
# my_s.split()
#
# orig_list = [1, 2, 3]   # с помощью copy()
# copy_list = orig_list.copy()
#
# my_list = [1, 2, 3] # объединение списков extend()
# another_list = [4, 5, 6]
# my_list.extend(another_list)
# print(my_list)

# my_list = []
# for i in range(10):
#     my_list.append(i)
# print(my_list)
#
# numbers = [x for x in range(10)]
# print(numbers)
#
# print([x for x in 'range(10)'])

# orig_list = [1, 2, 3, 4, 5]
#
# new_list = [x*2 for x in orig_list]
# print(new_list)

# num = [x for x in 'Игорь']
# print(num)
# print([x for x in 'Игорь'])

# words = ['игорь', 'маша', 'машинка']
# print([len(word) for word in words])

# revers_lst = [word[::-1] for word in words]
# print(revers_lst)

# capitalize_list = [name.capitalize() for name in words]
# print(capitalize_list)

# words = ['Python', 'лучше', 'всех']
# new_string = ' '.join([x.upper() for x in words])
# print(new_string)

# x = 5
# y = 5
# print('x равно y') if x == y  else print('x не рвано y')

# age = 9
# print('Подросток') if age < 10 else print('Взрослый')

# a = 10
# b = 20
# max_vlue = a if a > b else b
# print(max_vlue)

grade = 85
# if grade >= 90:
#     result = 'Прекрасно'
# elif grade >= 80:
#     result = 'Очень хорошо'
# elif grade >= 70:
#     result = 'Хорошо'
# elif grade >= 60:
#     result = 'Так себе'
# else:
#     result = 'Неудача'
# print(result)
# result = 'Прекрасно' if grade >=90 else 'Очень хорошо' \
#                                 if grade >= 80 else 'Хорошо' \
#                                 if grade >= 70 else 'Так себе' \
#                                 if grade >= 60 else 'Неудача'
# print(result)

# result  = [num for num in range(10) if num % 2 == 0]
#
# print(result)

res = ['Четное' if num % 2 == 0 else 'Нечетное' for num in range(10)]
print(res)