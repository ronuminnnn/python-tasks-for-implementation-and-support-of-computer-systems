# If3 protect. То же, но при нечисловом вводе выводится «Ошибка ввода»; ветки if не меняются
try:
    n = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    if n > 0:
        n += 1
    elif n < 0:
        n -= 2
    else:
        n = 10
    print(n)