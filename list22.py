# List22. Дан список A из N чисел и число D. Генератором вывести элементы, умноженные на D, и количество элементов, равных D
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
b = [x * d for x in a]
count = len([x for x in a if x == d])
print(b)
print(count)