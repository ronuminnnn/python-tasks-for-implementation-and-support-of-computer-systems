# List3. Дан список A из N чисел. Вывести сумму элементов и произведение элементов с чётными индексами (0, 2, 4...)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
p = 1
for i in range(n):
    s += a[i]
    if i % 2 == 0:
        p *= a[i]
print(s)
print(p)