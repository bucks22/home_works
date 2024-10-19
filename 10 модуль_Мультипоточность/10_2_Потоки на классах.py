import time
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power: int = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            days += 1
            time.sleep(1)
            print(f'{self.name} сражается {days} день(дня), осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 17)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')