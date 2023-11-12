# my_list = [1, 2, 1, 3, 3]
# my_list2 = my_list
# del my_list  # стереть объект из памяти
# print(my_list2)

# print(max(my_list))  #  максимальное значение

# print(min(my_list))  #  минимальное значение

# print(sum(my_list))  #  сумма всех элементов списка

# print(len(my_list))  #  дилна последовательности

# average = sum(my_list) / len(my_list)   #  поиск среднего значения
# print(average)

# reversed_id = reversed(my_list)  #  возвроащает обратную порядок элементов
# print(my_list)
# print(list(reversed_id))

# sor_list = sorted(my_list)  #  сортировка элементов от меньшего к большему
# print(sor_list)
#
# sor_list = sorted(my_list, reverse=True)  #  сортировка элементов от большего к меньшему
# print(sor_list)

# list1 = ['Б', 'А', 'Я', 'А', 'А']
# list2 = [2, 4, 3, 1, 1]

# list1.sort()  # Сортировка элементов по алфавиту
# list2.sort()  # Сортировка элементов по возрастанию
# print(list1)
# print(list2)

# print(list1.count('А'))  #  возвращает число повторений элементов в списке
# print(list2.count(1))  #  возвращает число повторений элементов в списке

# list1.clear()  #  очищает список
# print(list1)

# copied_list = list1.copy()
# print(copied_list)


#  Функции управлением товаром
def add_item(items, quantities):
    item_name = input('Введите название товара для добавления: ')
    quantity = int(input('Введите количество данного товара: '))

    if item_name in items:
        index = items.index(item_name)
        quantities[index] += quantity
    else:
        items.append(item_name)
        quantities.append(quantity)
def clear_items(items, quantities):
    choice = input('Вы УВЕРЕНЫ, что хотите отчистить список товаров(да/нет): ').lower()
    if choice == 'да':
        items.clear()
        quantities.clear()
        print('Список очищен')
def cout_item(items, quantities, item_name=''):
    if not item_name:
        item_name = input('Введите название товара для поиска: ')

    if item_name in items:
        index = items.index(item_name)
        return  quantities[index]

    else:
        return 0
# Функции статистики
def get_total_items(items, quantities):
    print('*Содержится на складе*')
    for i in range (len(items)):
        print(f' Товар {items[i]} в количестве {quantities[i]}')
def get_stats(items, quantities):
    pass


#  меню управления программой
def main():
    items = ['Игрушки', 'banana']
    quantities = [3, 5]

    while True:
        print('\n1: Добавить товар')
        print('2: Очистить список товаров')
        print('3: Посчитать определенный товар на складе')
        print('4: Показать общее количество товаров на складе')

        choice = input('Выберите действие: ')

        if choice == '1':
            add_item(items, quantities)
        elif choice == '2':
            clear_items(items, quantities)
        elif choice == '3':
            item_name = input('Введите название товара для подсчета: ')
            print(f'Товар {item_name} в наличии в количестве {cout_item(items, quantities, item_name)}')
        elif choice == '4':
            get_total_items(items,quantities)
        else:
            print('Неверный выбор. Пожалуйста выберите корректный пункт меню')


if __name__ == '__main__':
    main()