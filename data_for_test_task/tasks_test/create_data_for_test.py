"""здесь я создаю json файлики с тестами"""
import json
import time


def task1(a: int) -> str:  # 1
    """задача 1 про большое число"""
    if abs(a) > 1000000000:
        return 'Блин, реально большое число'
    if abs(a) <= 1000000000:
        return 'Хм, ну и мелкое конечно'


def task2(a: int) -> str:  # 2
    k = 1
    for i in range(1, int(a) + 1):
        k *= i
    return str(k)


def task3(n: int):  # 3
    rainbow = ("Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый")
    if n > 7:
        return "Радуга состоит только из семи цветов"
    else:
        lst = []
        for i in range(n):
            lst.append(rainbow[i])
        return lst


def task4(a: int) -> list:  # 4
    lst = []
    for i in range(1, a + 1):
        if i % 10 == 1 and i != 11:
            r = 'корова'
        elif 1 < i % 10 < 5 and not i in (12, 13, 14):
            r = 'коровы'
        else:
            r = 'коров'
        lst.append('На лугу ' + str(i) + ' ' + r)
    return lst


def task5(a: int) -> bool:
    """проверка на не чётность"""
    if a % 2 == 1:
        return True
    else:
        return False


def task6(a: int) -> list:
    "возвращает список квадратов от 1 до a включительно "
    lst = []
    for i in range(1, a + 1):
        lst.append(i ** 2)
    return lst


def task7(a: int) -> list:
    "возвращает список чисел до a включительно, которые являются степенями тройки"
    lst = []
    i = 0
    while True:
        if 3 ** i <= a:
            lst.append(3 ** i)
        else:
            break
        i += 1
    return lst


# lst = []
# start = time.time()
# for a in range(-7, 400, 29):
#     d = {(a): task6(a)}
#     lst.append(d)
# print(time.time() - start)
# print(lst)
# with open('test6.json', 'w') as file:
#     json.dump(lst, file, indent=4, ensure_ascii=False)
