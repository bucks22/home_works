class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, fn):
        self.name = name
        self.fn = int(fn)
    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')
        return

dom1 = House('Жк1', 12)
print(House.houses_history)
dom2 = House('Жк2', 32)
print(House.houses_history)
dom3 = House('Жк3', 42)
print(House.houses_history)

del dom2
del dom3
print(House.houses_history)