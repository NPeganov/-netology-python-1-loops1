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


if __name__ == '__main__':
    print('To stop entering boys\' names type "stop"!')
    boy_name = str()
    boys = set()
    while True:
        boy_name = input('Enter the name of a boy: ')
        if boy_name.lower() == 'stop':
            break
        else:
            boys.add(boy_name)

    print('To stop entering girls\' names type "stop"!')
    girl_name = str()
    girls = set()
    while True:
        girl_name = input('Enter the name of a girl: ')
        if girl_name.lower() == 'stop':
            break
        else:
            girls.add(girl_name)

    if len(girls) != len(boys):
        print("Attention, someone may be left without a pair!")
    else:
        print("The best pairs are:")
        for boy, girl in zip(sorted(boys), sorted(girls)):
            print(f"\n{boy.capitalize()} and {girl.capitalize()}")
