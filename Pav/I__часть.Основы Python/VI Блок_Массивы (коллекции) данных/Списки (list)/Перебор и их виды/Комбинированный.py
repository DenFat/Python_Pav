# fru = ['apple', True, 1]
#
# for index, value in enumerate(fru):
#     print(f'Элемент с индексом {index} имеет значение {value}')

# animals = ['кошка', 'собака', 'Игорь']
# for i in animals:
#     print(f'Животное {i} стоит у меня на месте по симпатии')
# print()
# animals = ['кошка', 'собака', 'Игорь']
# for i in range(len(animals)):
#     print(f'Животное {animals[i]} стоит у меня на месте {i+1} по симпатии')
# print()
# animals = ['кошка', 'собака', 'Игорь']
# for index, animal in enumerate(animals, start=1):
#     print(f'Животное {animal} стоит у меня на месте {index} по симпатии')


# numbers = [3,-1,4,-15,9,7,6,-8]
# negativ_list = []
#
# for index, value in enumerate(numbers):
#     if value < 0:
#         negativ_list.append(index)
# print(negativ_list)

my_list = ['apple', True, 123, False,4.56,'banana']

for index, value in enumerate(my_list):
    if isinstance(value, bool):
        pass
    if isinstance(value, str):
        pass
    if isinstance(value, int):
        pass
    if isinstance(value, float):
        pass