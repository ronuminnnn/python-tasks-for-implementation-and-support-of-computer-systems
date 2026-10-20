# Proc23. Функция quarter(x, y) возвращает номер координатной четверти точки с ненулевыми координатами. 
# Найти четверти трёх точек
def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(quarter(x1, y1))
print(quarter(x2, y2))
print(quarter(x3, y3))