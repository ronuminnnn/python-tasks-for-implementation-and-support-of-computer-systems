# For15. Дано вещественное число A и целое число N (> 0). Найти A в степени N: AN = A · A · ... · A (число A перемножается N раз).
a = float(input())
n = int(input())
total = 1
for i in range(n):
    total *= i
print(total)