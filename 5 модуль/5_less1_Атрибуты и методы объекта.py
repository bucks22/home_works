class House:
    def __init__(self, name, fn):
        self.name = name
        self.fn = int(fn)

    def go_to(self, nf):
        self.nf = int(nf)
        if self.nf > self.fn or self.nf < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, nf + 1):
                print(i)


dom1 = House('ЖК', 32)
dom2 = House('Ур', 2)
dom1.go_to(5)
dom2.go_to(6)
