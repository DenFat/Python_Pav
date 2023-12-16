# student_grade = {
#     'Алиса': {'математика': 90, 'наука': 88},
#     'Игорь': {'математика': 75, 'наука': 92},
# }

# alice_math_grade = student_grade['Алиса']['математика']
# print(f"Оценка алисы по математике: {alice_math_grade} баллов")
#
# alice_grades = student_grade['Алиса']
# print(alice_grades)

# Изменеие значения во вложенном словаре
# student_grade['Алиса']['математика'] = 100
# print(f'Обновленные данные по студенту Алиса {student_grade["Алиса"]["математика"]}')

# Добалвение нового предмета для Игоря
# student_grade['Игорь']['история'] = 85
# print(f'Оценки игоря {student_grade["Игорь"]}')

# Перебор всех студентов и их оценки
# for student, grades in student_grade.items():
#     print(f'Имя студента: {student}')
#     for subgect, grade in grades.items():
#         print(f'{subgect}: {grade}')
#     print()

# warehouse = {
#     'яблоки': {'количество': 150, 'цена': 50},
#     'Груши': {'количество': 120, 'цена': 60},
#     'апельсины': {'количество': 100, 'цена': 80}
# }
# warehouse['Бананы'] = {'количество': 110, 'цена': 30}
# print(warehouse)
#
# # Общаа стоимость товаров на складе
# for items,  details in warehouse.items():
#     total_cost = details['количество'] * details['цена']
#     print(f'{items}: {total_cost} рублей')
#
# # Удаление апельстнов со склада
# del warehouse['апельсины']
# print(warehouse)

def print_warehouse(warehouse, title='Состояние склада'):
    print(title)
    for item, details in warehouse.items():
        print(f'    {item}: {details}')
    print()

def add_to_warehouse(warehouse, item, quantity, price):
    warehouse[item] = {'количество': quantity, 'цена':price}
    print_warehouse(warehouse, title=f"Состояние склада после добавления {item}")

def uodatr_quantity_and_price(warehouse, item, quantity, price):
    if item in warehouse:
        pass

    else:
        print(f'Товара {item} не найден на складе')

warehouse = {
    'яблоки': {'количество': 150, 'цена': 50},
    'Груши': {'количество': 120, 'цена': 60},
    'апельсины': {'количество': 100, 'цена': 80}
}

print_warehouse(warehouse)
add_to_warehouse(warehouse, input('Введите название товара: '),
                 int(input('Введите количество товара: ')),
                 int(input('Введите цену товара за штуку: ')))



# Общаа стоимость товаров на складе
for items,  details in warehouse.items():
    total_cost = details['количество'] * details['цена']
    print(f'{items}: {total_cost} рублей')

# Удаление апельстнов со склада
del warehouse['апельсины']
print(warehouse)