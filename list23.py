# List23. Дан список A из N чисел. Вывести элементы в порядке убывания модуля (key=abs, reverse=True)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = sorted(a, key=abs, reverse=True)
print(b)