"""работающий класс"""

from typing import List, Dict
import json
from random import choice
from additional_function_for_time import time_limit, TimeoutException  # необходимый скрипт (зависимость)
import os
import os.path
from classes.remember import Remember


class TestTask(Remember):
    """класс, который проверяет работоспособность кода"""

    def __init__(self, cod: str, id: str):
        """принимает скрипт, который мы должны проверить и путь к файлику, где ответы находятся"""
        # with open(answers, 'r') as file:
        #     self.answers = json.load(file)

        self.cod = cod
        self.result_test = None  # результат теста

        # атрибут экземпляра для похвалы, когда человек напишет верный код)
        self.__praising = ['вааа, молодец, ты сделал правильно!!!', 'так деражть!!! Чел, ты крут!!!',
                           'оу, вот это зачётная программа', 'да ты супер крут, прям как курт, но не кобейн)))',
                           'ладно ладно, я понял, что ты могёшь всё:)', 'пушка, бомба, топчик, всё верно)',
                           'обалдеть ты умный, всё верно!']
        super().__init__(id=id)  # запускаем __init__ из наследуемого класса

    # def send_task_photo(self):  # возможно уберу, так как есть специально класс для работы с фотографиями
    #     """метод, который достаёт фотографию с заданием, которое нужно отправить"""
    #     self.photo_file = open(f'data_for_test_task/tasks_photos/test{self.tasks_done + 1}.png', 'rb')
    #     return self.photo_file

    def testCod(self) -> tuple:
        """запускаем тестирование кода """
        print(self.answers)
        if 'input()' in self.cod:
            self.result_test = (False, 'в функции не должно быть input()')
            return (False, 'в функции не должно быть input()')
        try:
            exec(self.cod)
        except SyntaxError as mistakeSyntax:  # если синтаксическая ошибка в коде, то возвращаем ошибку
            self.result_test = (False, str(mistakeSyntax).replace('<string>', 'str') +
                                '\nошибка в синтаксисе кода '
                                '(вспомни как писать код для функций, списков, словарей и так далее)')
            return (False, str(mistakeSyntax) +
                    '\nошибка в синтаксисе кода (вспомни как писать код для функций, списком, словарей и так далее')
        except NameError as mistakeName:
            self.result_test = (False, str(mistakeName).replace('<string>', 'str') + '\nне нашёл какую-то переменную')
            return (False, str(mistakeName) + '\nне нашёл какую-то переменную')

        # сначала удалим все переходы на следующую строку, которые до кода стоят
        try:
            while True:
                if self.cod[0] == '\n':
                    self.cod = self.cod[1:len(self.cod)]
                else:
                    break
        except IndexError:
            self.result_test = (False, 'хм, а где код?')
            return (False, 'хм, а где код?')

        # узнаём назавание функции, что бы запустить её
        self.name_func = self.cod[0:self.cod.find('\n')]
        if 'def ' not in self.name_func:
            self.result_test = (False, 'нет def в коде, исправляй, так как ты должен написать функцию')
            return (False, 'нет def в коде, исправляй, так как ты должен написать функцию')
        else:
            self.name_func = self.name_func[self.name_func.find('def ') + 4: self.name_func.find('(')]
            #  теперь надо убрать пробелы все после def и до названия функции
            while True:
                if self.name_func[0] == ' ':
                    self.name_func = self.name_func[1:len(self.name_func)]
                else:
                    break
        try:
            for i, test_dict in enumerate(self.answers):
                for test_valueKey in test_dict:
                    # проверим программку, что бы она выполнялась менее чем за секунду, иначе ошибка!!!
                    try:
                        with time_limit(1):
                            your_cod_output = eval(self.name_func + f'({test_valueKey})')
                    except TimeoutException as e:
                        self.result_test = (False, "Timed out!  СЛИШКОМ ДОЛГО работает")
                        return (False, "Timed out!  СЛИШКОМ ДОЛГО работает")
                    if your_cod_output != test_dict[test_valueKey]:
                        if i < 5:
                            response_to_the_user = f"тест {i + 1}\nтестовое значение: {test_valueKey}\n ответ твоего скрипта: {your_cod_output}\n" \
                                                   f"правильный ответ: {test_dict[test_valueKey]}"
                        else:
                            response_to_the_user = f'тест {i + 1} провален :('
                        self.result_test = (False, response_to_the_user)
                        return (False, response_to_the_user)
        except NameError as mistakeName:  # ошибка NameError, возвращаем её
            self.result_test = (False, str(mistakeName) + '\nне нашёл какую-то переменную')
            return (False, str(mistakeName) + '\nне нашёл какую-то переменную')
        self.result_test = (True,)
        return (True,)  # всё правильно

    def resultText(self):
        if self.result_test[0]:
            return choice(self.__praising)
        else:
            return self.result_test[1]


cod = """
def firstTasks_right(a) :
    if abs(a) > 1000000000:
        return 'Да, это большое число'
    if abs(a) <= 1000000000:
        return 'Нет, это не такое уж и большое число
"""

if __name__ == '__main__':
    p = TestTask(cod, 'data_for_test_task/test1.json')
    p.testCod()
    print(p.resultText())
