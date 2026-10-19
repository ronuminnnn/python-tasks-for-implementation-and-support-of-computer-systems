# List17. Дан список A из N чисел. Вывести элементы по возрастанию (sorted), затем исходный список без изменений
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = sorted(a)
print(b)
print(a)