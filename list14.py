# List14. Дан список A из N чисел и число D. Вывести число вхождений D (count) и индекс первого вхождения (или -1, если D нет)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
print(a.count(d))
if d in a:
    print(a.index(d))
else:
    print(-1)