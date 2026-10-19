# Proc15. Функция shift_left3(a, b, c) возвращает тройку после левого циклического сдвига: a на место c, c на место b, b на место a. Сдвинуть два набора
def shift_left3(a, b, c):
    return b, c, a
for i in range(2):
    a = int(input())
    b = int(input())
    c = int(input())
    print(*shift_left3(a, b, c))
