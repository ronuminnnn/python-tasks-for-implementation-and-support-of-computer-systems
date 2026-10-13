# For14. Дано N (> 0). Найти N2 по формуле: N2 = 1 + 3 + 5 + ... + (2·N −
n = int(input())
square = 0
for i in range(1, 2 * n, 2):
    square += i
print(square)