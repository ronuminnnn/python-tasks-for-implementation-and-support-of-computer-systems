# While11 protect. То же, но защищено чтение N: при нечисловом вводе выводится «Ошибка ввода»; цикл не меняется
try:
    n = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    k = 0
    s = 0
    while s < n:
        k += 1
        s += k
    print(k, s)