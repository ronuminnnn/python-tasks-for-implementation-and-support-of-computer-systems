# List19. Дан список из N строк. Вывести строки в порядке возрастания длины и отдельно самую длинную (max с key)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(sorted(a, key=len))
print(max(a, key=len))