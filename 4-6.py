from abc import ABC, abstractmethod


class Warehouse():
    storage:dict = {}
    def __init__(self):
        pass

    def add_equipment(self, equipment, count):
        equipment_type = equipment.__class__.__name__
        try:
            self.storage[equipment_type][equipment.name] += count
        except KeyError:
            if equipment_type not in self.storage:
                self.storage[equipment_type] = {}
                self.storage[equipment_type][equipment.name] = count
            elif equipment.name not in self.storage[equipment_type]:
                self.storage[equipment_type][equipment.name] = count

    def __str__(self):
        output = ''
        for k, equipment in self.storage.items():
            output += f'{k}:\n'
            for e, count in equipment.items():
               output += f'\t{e} {count}\n'
        return output

class Technics(ABC):

    def __init__(self, name, price, article):
        self.name = name
        self.price = price
        self.article = article
        count = 0

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except ValueError:
            print(f"price {price} is not a number")
            self.__price = None

    def __str__(self):
        return f'{self.name} {self.price}'


class Print(Technics):
    count = 0
    def __init__(self, name, price, article, colorprint):
        super().__init__(name, price, article)
        self.colorprint = colorprint
        Print.count += 1

class Scan(Technics):
    count = 0
    def __init__(self, name, price, article, multiscan):
        super().__init__(name, price, article)
        self.multiscan = multiscan
        Scan.count += 1

class Xerox(Technics):
    count = 0
    def __init__(self, name, price, article, industrial):
        super().__init__(name, price, article)
        self.industrial = industrial
        Xerox.count += 1


storage = Warehouse()

a1 = Print('Aboba', 200, '234sdf432', 'color')
a2 = Print('Steafu', 555, 'dsvfsd434', 'color+')
a3 = Print('Bobus', 234, '1233213', 'color')

storage.add_equipment(a1, 3)
storage.add_equipment(a2, 9)
storage.add_equipment(a3, 7)
print(storage)