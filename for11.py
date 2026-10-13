# For11. Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2·N)2.
N = int(input())
total = 0
for i in range(N, 2 * N + 1):
    total += i ** 2
print(total)