# Proc1. Описать функцию power_a3(a), возвращающую третью степень числа a. С помощью этой функции найти третьи степени пяти данных чисел.
def power_a3(a):
    return a ** 3
for i in range(5):
    a = float(input())
    print(power_a3(a))