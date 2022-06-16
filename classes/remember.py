import json
import os.path
import os


class Remember(object):
    def __init__(self, id):  # __init__ будет
        """проверяем есть ли этот пользователь уже в системе, если есть, то берём инофрмацию о том,
        что уже сделано, иначе создаём для него пустой json файл
        А ТАК ЖЕ СРАЗУ ПРОВЕРЯЕТ СКОЛЬКО ЗАДАНИЙ УЖЕ ВЫПОЛНЕННО"""
        self.id = id
        # если нет этого юзера, то создаём под него json файлик
        if not os.path.exists(f'remember_whats_done/{id}user'):
            self.whatsDoneAtr = []
            with open(f'remember_whats_done/{id}user', 'w') as file:
                json.dump(self.whatsDoneAtr, file, indent=4, ensure_ascii=False)
        else:
            with open(f'remember_whats_done/{id}user', 'r') as file:
                self.whatsDoneAtr = json.load(file)
        self.check_number()  # сразу запускаем проверку, сколько заданий уже сделал пользователь

    def check_number(self):
        """проверяет сколько заданий сделано, и заносит в self.answers ответы на следующее задание"""
        self.tasks_done = len(self.whatsDoneAtr)  # сколько заданий сделано
        try:
            with open(f'data_for_test_task/tasks_test/test{self.tasks_done + 1}.json', 'r') as file:
                self.answers = json.load(file)
        except FileNotFoundError as mistakeFileNotFound:
            print(mistakeFileNotFound, 'такого файла нет, возможно все задачи закончились')
            pass

    def updating_data(self, new: bool):
        """если пользователь выполнил правильно задание, то нужно закинуть в метод True и он сохранит эти данные"""
        if new:
            self.whatsDoneAtr.append(True)
            self.tasks_done = len(self.whatsDoneAtr)
            with open(f'remember_whats_done/{self.id}user', 'w') as file:
                json.dump(self.whatsDoneAtr, file, indent=4, ensure_ascii=False)

