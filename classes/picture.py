"""файл для работы с ихображениями
https://fixmypc.ru/post/vstavka-teksta-i-izobrazheniia-v-kartinku-s-python-pillow-pil/ - статья"""

from PIL import Image, ImageDraw, ImageFont
import os.path


class CreateTaskPhoto(object):
    def __init__(self, number_task: str, name_user: str):
        """создаёт картинку с заданием, по номеру задания и имени пользователя"""
        try:
            self.text_task = open(f'data_for_test_task/tasks_text/{number_task}.txt',
                              'r').read() + '\n\n\ninst: lev_repet\ngithub: Lev-Reyn'
        except Exception:
            self.text_task = open(f'data_for_test_task/tasks_text/finish.txt',
                                  'r').read() + '\n\n\ninst: lev_repet\ngithub: Lev-Reyn'
        self.neme_user = name_user
        self.im = Image.new('RGB', (1600, 100 + 45 * self.text_task.count('\n')), color=('#ffdd87'))
        self.font = ImageFont.truetype(  # шрифт
            'additionalFiles/fonts/ofont.ru_Roboto.ttf', size=40)  # добавляем шрифт
        self.draw_text = ImageDraw.Draw(self.im)
        self.draw_text.text(
            (20, 50),
            text=self.text_task,
            font=self.font,
            fill=('#1C0606')
        )
        # Откроет изображение в новом окне
        # im.show()
        print('lol---------')
        self.im.save(f'data_for_test_task/tasks_photos/test{number_task}.png')
        # self.im.save(f'test{number_task}.png')

        self.path_task_photo = f'data_for_test_task/tasks_photos/test{number_task}.png'

    def delete_photo(self):
        """метод удаляет фотографию"""
        import os
        if os.path.isfile(self.path_task_photo):
            os.remove(self.path_task_photo)
            print("success")
            self.path_task_photo = None  # то есть и ссылку тоже убираем, так как фотографии тоже ведь уже нет
        else:
            print("File doesn't exists!")
