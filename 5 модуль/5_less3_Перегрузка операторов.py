class House:
    def __init__(self, name, fn):
        self.name = name
        self.fn = int(fn)
    def __eq__(self, other):
        return self.fn == other.fn
    def __lt__(self, other):
        return self.fn < other.fn
    def __le__(self, other):
        return self.fn <= other.fn
    def __gt__(self, other):
        return self.fn > other.fn
    def __ge__(self, other):
        return self.fn >= other.fn
    def __ne__(self, other):
        return self.fn != other.fn

    def __add__(self, value):
        self.fn = self.fn + value
        return self.fn
    def __radd__(self, value):
        self.fn = self.fn + value
        return self.fn
    def __iadd__(self, value):
        self.fn += value
        return self.fn


    def go_to(self, nf):
        self.nf = int(nf)
        if self.nf > self.fn or self.nf < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, nf + 1):
                print(i)

    def __len__(self):
        return self.fn
    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.fn}')

dom1 = House('ЖК', 32)
dom2 = House('Ур', 32)
dom1.go_to(0)
dom2.go_to(6)

print(len(dom1))
print(len(dom2))
print(str(dom1))
print(str(dom2))

print(dom1 == dom2)
print(dom1 != dom2)
print(dom1 >= dom2)
print(dom1 <= dom2)
print(dom1 > dom2)
print(dom1 < dom2)

print(dom1.__add__(6))
print(dom1.__radd__(10))
print(dom1.__iadd__(15))