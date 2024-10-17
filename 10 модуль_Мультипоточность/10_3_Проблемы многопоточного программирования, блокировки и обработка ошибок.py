from time import sleep
import random
from threading import Thread, Lock

class Bank(Thread):
    def __init__(self):
        super().__init__()
        # self.balance: int = balance
        self.lock = Lock()


    def deposit(self):
        self.balance = 0
        for i in range(100):
            self.rand_dep = random.randint(50, 500)
            self.balance += self.rand_dep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {self.rand_dep}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for k in range(100):
            self.rand_take = random.randint(50, 500)
            print(f'Запрос на {self.rand_take}')
            if self.rand_take <= self.balance:
                self.balance -= self.rand_take
                print(f'Снятие: {self.rand_take}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
