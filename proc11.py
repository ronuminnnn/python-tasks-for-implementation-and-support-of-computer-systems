# Proc11.Функция minmax(x, y) возвращает пару (меньшее, большее). 
# Четырьмя вызовами найти минимум и максимум четырёх данных чисел A, B, C, D
def minmax(x, y):
    if x < y:
        return x, y
    else:
        return y, x
a = float(input())
b = float(input())
c = float(input())
d = float(input())
min1, max1 = minmax(a, b)
min2, max2 = minmax(c, d)
minimum, other1 = minmax(min1, min2)
other2, maximum = minmax(max1, max2)
print(minimum)
print(maximum)