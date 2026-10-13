# For13. Дано целое число N (> 0). Найти значение выражения 1.1 − 1.2 + 1.3 − ... (N слагаемых, знаки чередуются).
N = int(input())
total = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        total += 1 + i / 10
    else:
        total -= 1 + i /10
print(total)