from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name: str = name
        self.weight: float = weight
        self.category: str = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self, __file_name):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.file = open(self.__file_name, 'r')
        existing_products = self.file.read()
        self.file.close()
        return existing_products.splitlines()

    def add(self, *products):
        product_in_list = self.get_products()
        self.file = open(self.__file_name, 'a')

        for product in products:
            if product.name in [p.split(',')[0] for p in product_in_list]:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                self.file.write(str(product) + '\n')
        self.file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())