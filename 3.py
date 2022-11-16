class ValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


mylist = []
el = ''
while el != 'stop':
    el = input("Введите элемент: ")

    try:
        if not el.isdigit():
            raise ValueError("Вводить можно только числа")
    except ValueError as err:
        print(err)
    else:
        mylist.append(el)

print(mylist)
