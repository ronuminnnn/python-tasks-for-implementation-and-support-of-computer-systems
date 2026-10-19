# List9. Дан список A из N чисел. Вывести элементы, большие среднего арифметического всех элементов, и их количество
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
for x in a:
    s += x
average = s / n
b = []
for x in a:
    if x > average:
        b.append(x)
print(b)
print(len(b))