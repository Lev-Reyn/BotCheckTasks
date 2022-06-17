"""сейчас я в TestBranchMyBotTaskV1"""
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from additionalFiles.config import token
from classes.main_funcs_oop_try import TestTask
from classes.picture import CreateTaskPhoto  # класс для работы с созданием фотографий с заданиями

bot = Bot(token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_process_command(message: types.Message):
    """начало работы бота"""
    await message.delete()
    # возможно при команде старт я сделаю полный презапуск, а возможно нет
    await bot.send_message(message.from_user.id, 'типо тут задание (обязательно вводить функции)')
    task = CreateTaskPhoto(number_task='1', name_user=message.from_user.id)  # лучше бы потом вставить id пользователя
    await bot.send_photo(message.from_user.id, photo=open(task.path_task_photo, 'rb'))
    # task.delete_photo()  # пока что не удаляем


@dp.message_handler()
async def fill_in_the_schedule_process_message(message: types.Message):
    """обрабатывает сообщения |  и я сделаю так, что всегда будет проверять первую строку, и если там определённая
     команда, то вызывается определённая функция"""
    # p_remember = Remember()
    # p_remember.test_user(message.from_user.id)  # проверяем, есть ли там id
    # if '# 1' in message.text:
    #     p = TestTask(cod=message.text, answers='data_for_test_task/tasks_test/test1.json')
    # elif '# 2' in message.text:
    #     p = TestTask(cod=message.text, answers='data_for_test_task/tasks_test/test2.json')
    # elif '# 3' in message.text:
    #     p = TestTask(cod=message.text, answers='data_for_test_task/tasks_test/test3.json')
    # elif '# 4' in message.text:
    #     p = TestTask(cod=message.text, answers='data_for_test_task/tasks_test/test4.json')
    # else:
    #     p = TestTask(cod='no cod', answers='data_for_test_task/tasks_test/test1.json')  # пока что тест, фигня
    p = TestTask(cod=message.text, id=message.from_user.id)

    await bot.send_message(message.from_user.id, 'проверяю...')
    p.testCod()
    p.updating_data(p.result_test[0])
    await bot.send_message(message.from_user.id, f'{p.resultText()}')
    if p.result_test[0]:
        task = CreateTaskPhoto(p.tasks_done + 1, message.from_user.id)  # создаём фотографию с заданием
        await bot.send_photo(message.from_user.id, photo=open(task.path_task_photo, 'rb'))  # отправляем фотографию с заданием
        task.delete_photo()  # удаляем фотографию с заданием


executor.start_polling(dp)
