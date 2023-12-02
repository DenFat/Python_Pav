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