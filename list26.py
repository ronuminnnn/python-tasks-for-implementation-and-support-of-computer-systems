# List26. Дан список A из N чисел. Генератором вывести элементы, большие среднего, и само среднее
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
average = sum(a) / len(a)
b = [x for x in a if x > average]
print(f"{average:.1f}")
print(b)