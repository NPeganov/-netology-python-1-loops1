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
    if len(word) % 2 == 1:
        a = len(word) // 2
        let = word[a]
    else:
        a = len(word) // 2
        let = word[a - 1:a + 1]

    print(let)
