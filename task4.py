"""
Задание 4
У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам
(структура данных в примере). Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!)
для каждой страны.

Пример работы программы:

countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]], ###################### ~ 74.942857
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
Результат:

Средняя температура в странах:
Таиланд  -  23.9 С
Германия  -  13.8 С
Россия  -  3.7 С
Польша  -  12.0 С

"""


TEST_INPUT_DATA = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]


def convert_f_to_c(temperature_f):
    """This function converts temperature in F into temperature in C"""
    if isinstance(temperature_f, float) or isinstance(temperature_f, int):
        F_TO_C_KEY = 33.8
        return temperature_f * F_TO_C_KEY
    else:
        print("Wrong input parameter, a number was expected")


if __name__ == '__main__':
    print("Average temperature in countries:")
    for country_and_temperature in TEST_INPUT_DATA:
        country = country_and_temperature[0]
        temperature = country_and_temperature[1]
        avg_temp_f = sum(temperature) / len(temperature)
        avg_temp_c = convert_f_to_c(avg_temp_f)
        print(f"{country} - {avg_temp_c} C")
