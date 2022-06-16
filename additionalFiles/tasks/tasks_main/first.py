
def firstTasks_right(a: int) -> str:
    if abs(a) > 1000000000:
        return 'Да, это большое число'
    if abs(a) <= 1000000000:
        return 'Нет, это не такое уж и большое число'


"""здесь основные функции, которые потребуются данному боту"""


def take_name_funcs(cod: str) -> str:
    """функция принимает: код функции в строкрвом виде
    и достаёт назваание функции, которую создал человек"""


    # сначала удалим все переходы на следующую строку, которые до кода стоят
    while True:
        if cod[0] == '\n':
            cod = cod[1:len(cod)]
        else:
            break

    # узнаём назавание функции, что бы запустить её
    name_func = cod[0:cod.find('\n')]
    if 'def ' not in name_func:
        print('нет def в коде, исправляй')
    else:
        name_func = name_func[name_func.find('def ') + 4: name_func.find('(')]
        #  теперь надо убрать пробелы все после def и до названия функции
        while True:
            if name_func[0] == ' ':
                name_func = name_func[1:len(name_func)]
            else:
                break
    # name_func += '(-3100000000)'
    return name_func
    # exec('a = ' + name_func)
    # print(a)


def test_firstTasks(cod: str) -> bool:
    name_func = take_name_funcs(cod) # получаем название функции из кода
    func_of_student = 'пусто'
    for i in range(-10000000000, 10000000000, 10000000):
        func_of_student = 'func_of_student = ' + name_func + f'({i})'
        func_of_student = cod + '\n' + func_of_student
        print(func_of_student)
        exec(func_of_student)
        if firstTasks_right(i) != func_of_student:
            return False
    return True

# print(test_firstTasks("""
# def firstTasks_rightblin(a: int) -> str:
#     if abs(a) > 1000000000:
#         return 'Да, это большое число'
#     if abs(a) <= 1000000000:
#         return 'Нет, это не такое уж и большое число'
# """))

for i in range(-10000000000, 10000000000, 10000000):
    cod = """
def firstTasks_rightblin(a: int) -> str:
    if abs(a) > 1000000000:
        return 'Да, это большое число'
    if abs(a) <= 1000000000:
        return 'Нет, это не такое уж и большое число'
    """
    exec(cod)
    exec(f'lol = {take_name_funcs(cod)}({i})')

    if lol == firstTasks_right(i):
        print('wow')
    else:
        print('blin')
    print(lol)