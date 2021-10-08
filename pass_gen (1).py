import random


avalaible_symbols = r'1234567890lkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#!'


def get_number():
    while True:
        try:
            num = int(input())
        except ValueError:
            num = -1

        if num > 0:
            break  
        print('Нужно ввести положительное целое число!')

    return num


def generate_password(min_length, max_length):
    pass_len = random.randint(min_length, max_length)  
    password = ''
    for i in range(1, pass_len + 1):  # +1 потому что правая граница в range не включена
        random_pos = random.randint(1, len(avalaible_symbols))  # получить случайный индекс из строки символов
        ch = avalaible_symbols[random_pos - 1]  # т.к. отсчет с 0 и до длины строки -1
        password = password + ch

    return password


def main():
    while True:
        print('Введите минимальное количество символов в пароле.')
        min_length = get_number()

        print('Введите максимальное количество символов в пароле.')
        max_length = get_number()
        if min_length <= max_length:
            break

        print('Максимальное количество символов не может быть меньше минимального количества!')

    password = generate_password(min_length, max_length)
    print(f'Сгенерированный пароль: >>> {password} <<<  Не говорите его никому! :)')


if __name__ == '__main__':
    main()
