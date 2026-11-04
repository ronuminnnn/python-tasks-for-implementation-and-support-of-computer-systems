# String4. Дано N (1 ≤ N ≤ 26). Вывести строку из N первых заглавных латинских букв
n = int(input())
s = ""
for i in range(n):
    s += chr(ord("A") + i)
print(s)