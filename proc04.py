# Proc4. Функция triangle_ps(a) возвращает периметр P = 3·a и площадь S = a2·√3/4 равностороннего треугольника. 
# Найти P и S трёх данных сторон
import math
def triangle_ps(a):
    p = 3 * a
    s = a ** 2 * math.sqrt(3) / 4
    return p, s
for i in range(3):
    a = float(input())
    print(triangle_ps(a))