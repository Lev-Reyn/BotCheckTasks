from typing import List, Dict
import json

cod_input = """
def lol(a):
    a = int(a)
    if a == -2000000000:
        return("Да, это большое число")
    elif a == -1000000000:
        return("Нет, это не такое уж и большое число")  
    elif a == 0:
        return("Нет, это не такое уж и большое число")
    elif a == 1000000000:
        return("Нет, это не такое уж и большое число")
    elif a == 2000000000:
        return("Да, это большое число")  
    elif a == 3000000000:
        return("Да, это большое число")  
"""


def testFunc(cod: str, answers: List[Dict]) -> tuple:
    # cod_input = input()

    if 'input()' in cod:
        return (False, 'в функции не должно быть input()')
    try:
        exec(cod)
    except SyntaxError as mistakeSyntax:  # если синтаксическая ошибка в коде, то возвращаем ошибку
        return (False, 'error', mistakeSyntax,
                'ошибка в синтаксисе кода (вспомни как писать код для функций, списком, словарей и так далее')

    # сначала удалим все переходы на следующую строку, которые до кода стоят
    try:
        while True:
            if cod[0] == '\n':
                cod = cod[1:len(cod)]
            else:
                break
    except IndexError:
        return (False, 'хм, а где код?')

    # узнаём назавание функции, что бы запустить её
    name_func = cod[0:cod.find('\n')]
    if 'def ' not in name_func:
        return (False, 'нет def в коде, исправляй, так как ты должен написать функцию')
    else:
        name_func = name_func[name_func.find('def ') + 4: name_func.find('(')]
        #  теперь надо убрать пробелы все после def и до названия функции
        while True:
            if name_func[0] == ' ':
                name_func = name_func[1:len(name_func)]
            else:
                break
    try:
        for i, test_dict in enumerate(answers):
            for test_valueKey in test_dict:
                your_cod_output = eval(name_func + f'({test_valueKey})')
                if your_cod_output != test_dict[test_valueKey]:
                    if i < 5:
                        response_to_the_user = f"тест {i + 1}\nтестовое значение: {test_valueKey}\n ответ твоего скрипта: {your_cod_output}\n" \
                                               f"правильный ответ: {test_dict[test_valueKey]}"
                    else:
                        response_to_the_user = f'тест {i + 1} провален :('
                    return (False, response_to_the_user)
    except NameError as mistakeName:  # ошибка NameError, возвращаем её
        return (False, str(mistakeName) + 'не нашёл какую-то переменную')
    return (True,)  # всё правильно


with open('data_for_test_task/tasks_test/test1.json') as file:
    answers = json.load(file)

print(testFunc(cod=cod_input, answers=answers))
