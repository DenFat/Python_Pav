from Color import *
from PlayerChoice import get_answer
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


if __name__ == '__main__':
    main()