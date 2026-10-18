# Begin8 protect. То же, но при нечисловом вводе выводится «Ошибка ввода» вместо ответа; порядок и формула прежние.
try:
    a = float(input())
    b = float(input())
except ValueError:
    print("Ошибка ввода")
else:
    print((a + b) / 2)