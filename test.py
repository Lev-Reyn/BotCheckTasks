import json


def korova(n):
    lst = []
    if n == 0:
        return []
    else:
        if n == 1:
            lst.append('На лугу 1 корова')
        elif 1 < n <= 4:
            lst.append('На лугу 1 корова')
            for i in range(2, n + 1):
                lst.append('На лугу ' + str(i) + ' коровы')
        else:
            lst.append('На лугу 1 корова')
            for i in range(2, 5):
                lst.append('На лугу ' + str(i) + ' коровы')
            for i in range(5, n + 1):
                lst.append('На лугу ' + str(i) + ' коров')
        return lst

with open('data_for_test_task/tasks_test/test4.json') as file:
    answers = json.load(file)

for i, elem in enumerate(answers):
    for key in elem:
        print(i, key, korova(int(key)), elem[key])
