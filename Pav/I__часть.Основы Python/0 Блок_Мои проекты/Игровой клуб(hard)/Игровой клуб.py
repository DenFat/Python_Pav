from colorama import Fore, init
init(autoreset=True)
def get_answer(digit, message):       # Проверка на корректный ответ пользователя
    answer = ''
    while answer not in digit or answer == '':
        answer = input(message)
    return answer



def get_rate(minimum, maximum,message):     # Проверка ставки на корректность
    rate = -1
    while rate < minimum or rate > maximum:
        answer = input(message)

        if answer.isdigit():
            rate = int(answer)
            if rate > maximum:
                print(Fore.RED + "У вас не достоаточно денег для  ставки!\n")
        else:
            print(Fore.RED + "Введите корректное число для ставки\n")
    return rate


print(get_rate(1, 1000, Fore.GREEN + 'Сдлеайте савку от 1 до 1000 рублей: '))


def color(color_number):        # Определение номера цвета текста
    if color_number == 1:
        return Fore.BLACK
    elif color_number == 2:
        return Fore.RED
    elif color_number == 3:
        return Fore.GREEN
    elif color_number == 4:
        return Fore.YELLOW
    elif color_number == 5:
        return Fore.BLUE
    elif color_number == 6:
        return Fore.MAGENTA
    elif color_number == 7:
        return Fore.CYAN
    else:
        return Fore.WHITE


def colorText(color_number, line):      # вывод информации в цвете
    print(color(color_number) + line)




def victory(result):      # реакция на победу
    pass


def loss(result):     # реакция на проигрыш
    pass

def main():
    colorText(7, f'{" "*35}Добро пожаловать в "Игровой клуб"')
    print(color(6) + '\n1. Слот-машина')
    print(color(6) + '2. Выход')

    player_choice = (get_answer('1, 2', 'Выберите нужный пункт меню: '))
    # print(get_rate(1, 1000, Fore.GREEN + 'Сдлеайте савку от 1 до 1000 рублей: '))
    if player_choice == '1':
        pass
    elif player_choice == '2':
        print('Всего хорошего! Ждем обратно')

main()