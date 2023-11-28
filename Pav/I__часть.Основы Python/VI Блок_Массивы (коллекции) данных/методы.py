# my_dict = {'a': 1, 'b': 2, 'c':3}
# value = my_dict.get('b')
# print(value)

# value = my_dict.get('d', 'ключ не найден')
# print(value)

# print(my_dict.keys())
# for key in my_dict.keys():
#     print('ключ: ', key, 'значение: ', my_dict[key])

# print(my_dict.values())
# for values in my_dict.values():
#     print(values)

# min_value = min(my_dict.values())
# max_value = max(my_dict.values())
# # print(f'Минимальное значение {min_value}\nМаксимальное значение {max_value}')
#
# print(my_dict.items())
# for key, value in my_dict.items():
#     print(f'{key}{value}')


# my_dict = {30: 1, 25: 2, 50: 3}
# print(sorted(my_dict))      #   Сортировка по ключу
# print(sorted(my_dict.values()))     #   Сортировка по значению
# print(sorted(my_dict.items()))      #   Сортировка по ключу


# my_dict = {'A': 1, 'B': 2, 'C': 3}
# del my_dict['A']
# print(my_dict)
#
# del my_dict
# print(my_dict)

# name = input('Введите ваше имя: ')
# age = input('Введите ваш возраст: ')
# color = input('Введите ваш любимый цвет: ')
#
# user_info = {
#     'Имя': name,
#     'Возраст': age,
#     'Цвет': color
# }
# for key, value, in user_info.items():
#     print(key + ':', value)

# my_dict = {}
# for i in 'Лев Николаевич Толстой':
#     # if i in my_dict:
#     #     my_dict[i] += 1
#     # else:
#     #     my_dict[i] = 1
#     if i not in my_dict:
#         my_dict[i] = 1
#     else:
#         my_dict[i] += 1
# for key, value in my_dict.items():
#     print(f" Символ '{key}' встречается в тексте {value} раз")


names_and_ages = [
    'Иван 25',
    'Мария 30',
    'Игорь 40',
    'Светлана 20'
]
def names_in_age(lst):
    name_age_dict = {}
    for i in lst:
        name, age = i.split()
        name_age_dict[name] = int(age)
    return name_age_dict

def checkDict(dict, ageMin, ageMax):
    for key, value in dict.items():
        if value >=ageMin and value <= ageMax:
            print(key + ':', value)
nameDict = names_in_age(names_and_ages)
checkDict(nameDict, 25, 35)