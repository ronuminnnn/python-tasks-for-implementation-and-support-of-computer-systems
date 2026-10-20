# Proc25. Функция is_square(k) возвращает True, если k (> 0) — квадрат целого числа. 
# Найти количество квадратов в наборе из 10 чисел
def is_square(k):
    return int(k ** 0.5) ** 2 == k
count = 0
for i in range(10):
    k = int(input())
    if is_square(k):
        count += 1
print(count)