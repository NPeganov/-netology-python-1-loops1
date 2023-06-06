"""
Задание 1
Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:

среднюю букву, если число букв в слове нечетное;
две средних буквы, если число букв четное.
Примеры работы программы:

word = 'test'
Результат:
es

word = 'testing'

Результат:
t
"""


if __name__ == '__main__':
    word = input("Enter the word: ")
    length = len(word)
    a = length // 2
    result = None
    if length % 2 == 1:
        result = word[a]
    else:
        result = word[a - 1:a + 1]

    print(result)
