print("11 — север, 12 — запад, 13 — юг, 14 — восток")
north = 11
west = 12
south = 13
east = 14
start = int(input("Введите исходное положение: "))
print("Команды: цифровые команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо ") 
if start == north:
    start == "север"
    print("направление: север")
elif start == west:
    print("направление: запад")
elif start == south:
    print("направление: юг")
elif start == east:
    print("направление: восток")
else:
    print("Неправильное направление")
n = int(input("Введите команду: "))
if n == 0:
    if start == 12:
            print("Движение в направлении:запад")
    elif start == 13:
        print("Движение в направлении:юг")
    elif start == 14:
        print("Движение в направлении:воствок")
    elif start == 11:
        print("Движение в направлении:север")
elif n == 1:
    start = start + 1
    if start == 11:
        print("Движение в направлении:север")
    elif start == 12:
        print("Движение в направлении:запад")
    elif start == 13:
        print("Движение в направлении:юг")
    elif start == 14:
        print("Движение в направлении:воствок")
    elif start == 11:
        print("Движение в направлении:север")
elif n == -1:
    start = start - 1
    if start == 12:
        print("Движение в направлении:запад")
    elif start == 13:
        print("Движение в направлении:юг")
    elif start == 10:
        print("Движение в направлении:восток")
    elif start == 11:
        print("Движение в направлении:север")
else:
    print("нет такого закона")