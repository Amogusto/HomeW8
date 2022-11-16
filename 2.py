class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_int = int(input("Введите делитель: "))
my_div = int(input("Введите делимое: "))

try:
    if my_int == 0:
        raise ZeroError("Деление на ноль!")
except ZeroError as err:
    print(err)
else:
    print(my_div / my_int)