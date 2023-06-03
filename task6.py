"""

Задание 6 (необязательное)
Необходимо у пользователя запрашивать набор чисел разделенных пробелом. В результате в отсортированном порядке должны
выводиться числа, которые повторяются в вводе более одного раза.

Примеры работы программы:

Введите числа:
4 8 0 3 4 2 0 3
Результат:
0 3 4

Введите числа:
1 1 2 2 3 3
Результат:
1 2 3

Введите числа:
10 15 15 103 200 200 200 1 1 1 1 1 2 2 2
Результат:
1 2 15 200

"""

import re


def insert(input_string=None):
    if not input_string:
        input_string = input("Enter numbers separated by a space: ")

    regex1 = r'\D' # Ищем любые символы, кроме чисел и пробелов
    regex2 = r' {2,}' # Ищем 2 и более пробелов
    match1 = match2 = True

    while True:
        # Если ничего, кроме одинарных пробелов и цифр не нашли, то ввод корректен
        if not (re.search(regex1, input_string) or re.search(regex2, input_string)):
            break

        print('Wrong enter')

    raw_numbers = input_string.split(" ")
    unique_numbers = sorted(set(input_string.split(" ")), key=int)
    result_string = str()

    for number in unique_numbers:
        if raw_numbers.count(number) > 1:
            result_string += "".join(f"{number} ")

    return result_string.strip()


if __name__ == '__main__':

    print(insert())

    # if "1 2 15 200" == insert("10 15 15 103 200 200 200 1 1 1 1 1 2 2 2"):
    #     print("Hooray")
    # else:
    #     print('Fail')