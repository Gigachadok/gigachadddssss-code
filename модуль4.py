import os
import time


class DataPrank:

    def __init__(self, delay):
        self.delay = delay
        # Находим путь к папке data, которая лежит рядом с нашей программой
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sound = os.path.join(base_dir, "data", "fart.mp3")
        self.image = os.path.join(base_dir, "data", "arc.jpg")

    def activate(self):
        # Ждем в засаде
        time.sleep(self.delay)

        # Момент взрыва
        try:
            if os.path.exists(self.sound):
                os.startfile(self.sound)
            if os.path.exists(self.image):
                os.path.exists(self.image)
                os.startfile(self.image)
        except:
            pass


troll_bot = DataPrank(delay=5)
troll_bot.activate()

