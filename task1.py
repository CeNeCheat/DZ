days = int(input("Количество дней: "))
var1 = float(input("Скидка: "))
var2 = float(input("Цена: "))
if var1 == 0:
    var1 = 100
elif var1 == 100:
    var1 = 0
var1 = var1 * 0.01
var2 = var2 + days * 3
var2 = var2 * var1
print("итоговая сумма:", var2)