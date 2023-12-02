from random import randint
from time import sleep
from Color import *
def AnimationSlotMachine():  # Анимация барабана
    cell_digit_1 = 0  # ячейка № 1
    cell_digit_2 = 0  # ячейка № 2
    cell_digit_3 = 0  # ячейка № 3
    cell_digit_4 = 0  # ячейка № 4
    cell_digit_5 = 0  # ячейка № 5

    get_cell_digit_1 = True  # Логическая переменная для остановки 1 ячейки
    get_cell_digit_2 = True  # Логическая переменная для остановки 2 ячейки
    get_cell_digit_3 = True  # Логическая переменная для остановки 3 ячейки
    get_cell_digit_4 = True  # Логическая переменная для остановки 4 ячейки
    get_cell_digit_5 = True  # Логическая переменная для остановки 5 ячейки

    while get_cell_digit_1 or get_cell_digit_2 or get_cell_digit_3 or \
        get_cell_digit_4 or get_cell_digit_5:

        if get_cell_digit_1:  # Если переменная отвечающая за превую ячеку True, то...
            cell_digit_1 += 1  # увеличить значение ячейки №1
            if cell_digit_1 > 9:
                cell_digit_1 = 0
        if get_cell_digit_2:
            cell_digit_2 -= 1
            if cell_digit_2 < 0:
                cell_digit_2 = 9
        if get_cell_digit_3:
            cell_digit_3 += 1
            if cell_digit_3 > 9:
                cell_digit_3 = 0
        if get_cell_digit_4:
            cell_digit_4 -= 1
            if cell_digit_4 < 0:
                cell_digit_4 = 9
        if get_cell_digit_5:
            cell_digit_5 += 1
            if cell_digit_5 > 9:
                cell_digit_5 = 0

        if randint(0, 20) == 1:
            get_cell_digit_1 = False
        if randint(0, 20) == 1:
            get_cell_digit_2 = False
        if randint(0, 20) == 1:
            get_cell_digit_3 = False
        if randint(0, 20) == 1:
            get_cell_digit_4 = False
        if randint(0, 20) == 1:
            get_cell_digit_5 = False

        sleep(0.1)
        print(Fore.CYAN + f' {cell_digit_1}' + Fore.MAGENTA+ f' {cell_digit_2}' + Fore.YELLOW + f' {cell_digit_3 }' +
              Fore.GREEN + f' {cell_digit_4}' + Fore.RED + f' {cell_digit_5}')


def GetMaxCount(digit, cell_1, cell_2, cell_3, cell_4, cell_5):  # Подсчет количества совпадений чисел в барабане
    count = 0
    if digit == cell_1:
        count += 1
    if digit == cell_2:
        count += 1
    if digit == cell_3:
        count += 1
    if digit == cell_4:
        count += 1
    if digit == cell_5:
        count += 1
    return count
AnimationSlotMachine()