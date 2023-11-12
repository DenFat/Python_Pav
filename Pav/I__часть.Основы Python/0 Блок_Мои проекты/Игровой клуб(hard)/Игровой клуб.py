from colorama import Fore, init
init(autoreset=True)
def get_answer(digit, message):       # Проверка на корректный ответ пользователя
    answer = ''
    while answer not in digit or answer == '':
        answer = input(message)
    return answer



print(get_answer('1, 2', 'Выберите нужный пункт меню: '))


def get_rate(minimum, maximum,message):     # Проверка ставки на корректность
    pass


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


for i in range(1,9):
    colorText(i, 'Текст')

def victory(result):      # реакция на победу
    pass


def loss(result):     # реакция на проигрыш
    pass