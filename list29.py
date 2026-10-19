# List29. Дан список A из N чисел и число K. Вывести K наибольших элементов в порядке убывания (сортировка плюс срез)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
b = sorted(a, reverse=True)
print(b[:k])