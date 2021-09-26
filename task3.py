import datetime
x = int(input("Введите год1: "))
y = int(input("Введите месяц1: "))
z = int(input("Введите день1: "))
date1 = datetime.date(x, y, z)
x1 = int(input("Введите год2: "))
y1 = int(input("Введите месяц2: "))
z1 = int(input("Введите день2: "))
date2 = datetime.date(x1, y1, z1)
if date1 < date2:
    print("yes")
elif date1 > date2:
    print("no")