x = int
num = 237
#Т.к. число xyz - z = xy0,
# значит числа z и xy мы можем найти при помощи деления
# на цело и при помощи деления с выводом остатка
numlast = num // 100
print("Последняя цифра:", numlast)  
numdel10 = num % 100
print("Число после деления: ", numdel10) 
x = numdel10 * 10 + numlast
print("Число:", x)