from colorama import Fore, init
init(autoreset=True)
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