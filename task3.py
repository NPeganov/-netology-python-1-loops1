"""
Задание 3
Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с
одинаковыми индексами после сортировки! Но мы не будем никого знакомить, если кто-то может остаться без пары:

Примеры работы программы:

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
Результат:

Идеальные пары:
Alex и Emma
Arthur и Kate
John и Kira
Peter и Liza
Richard и Trisha

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
Результат:

Внимание, кто-то может остаться без пары!
"""

STOP_NAME = 'stop'

if __name__ == '__main__':
    print('To stop entering boys\' names type "stop"!')
    boy_name = str()
    boys = set()  # Мы используем здесь set, чтобы исключить повторение имён
    # В задании это явно не указано, но я сознательно решил ввести ограничение на уникальность имен

    while boy_name.lower() != STOP_NAME:
        boy_name = input('Enter the name of a boy: ')
        boys.add(boy_name.lower())  # Мы используем здесь lower(), также чтобы исключить повторение имён

    boys.remove(STOP_NAME)  # Для того, чтобы 'stop' не входило в итоговый список имён

    print('To stop entering girls\' names type "stop"!')
    girl_name = str()
    girls = set()
    while girl_name.lower() != STOP_NAME:
        girl_name = input('Enter the name of a girl: ')
        girls.add(girl_name.lower())

    girls.remove(STOP_NAME)

    if len(girls) != len(boys):
        print("Attention, someone may be left without a pair!")
    else:
        print("The best pairs are:")
        for boy, girl in zip(sorted(boys), sorted(girls)):
            print(f"\n{boy.capitalize()} and {girl.capitalize()}")
