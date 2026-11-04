# Matrix6. Даны M, N, число Q и набор из N чисел. 
# Первая строка — набор; каждая следующая строка равна предыдущей, умноженной на Q по столбцам
m = int(input())
n = int(input())
q = int(input())
values = [int(x) for x in input().split()]
a = [values[:]]
for i in range(1, m):
    a.append([x * q for x in a[i - 1]])
for row in a:
    print(row)