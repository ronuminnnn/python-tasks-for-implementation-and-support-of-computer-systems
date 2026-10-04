# Boolean15. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными».
a = int(input())
b = int(input())
c = int(input())
print((a > 0 and b > 0 and c <= 0) or (a > 0 and c > 0 and b <= 0) or (b > 0 and c > 0 and a <= 0))