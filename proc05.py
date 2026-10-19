# Proc5. Функция rect_ps(x1, y1, x2, y2) возвращает периметр и площадь прямоугольника со сторонами, параллельными осям, по противоположным вершинам. 
# Найти P и S трёх прямоугольников
def rect_ps(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    p = 2 * (a + b)
    s = a * b
    return p, s
for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    print(rect_ps(x1, y1, x2, y2))