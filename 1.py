class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def constr(cls, mystr):
        d, m, y = mystr.split("-")
        return cls(d, m, y)

    @staticmethod
    def valid(obj):
        d, m, y = (obj.split("-"))
        d = int(d)
        m = int(m)
        y = int(y)
        c = 0
        if d < 1 or d > 31:
            c += 1
            print("Не верно указан день")
        if m < 1 or m > 12:
            c += 1
            print("Не верно указан месяц")
        if y < 1900 or y > 2050:
            c += 1
            print("Не верно указан год")
        if c == 0:
            print("Ошибок нет")

    def __str__(self):
        return f'{self.d}.{self.m}.{self.y}'
a = Date.valid("18-05-1998")

a = Date.constr("18-05-1998")

print(a)
