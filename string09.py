# String9. Даны чётное N (> 0) и символы C1, C2. Вывести строку длины N из чередующихся C1 и C2, начиная с C1
n = int(input())
c1 = input()
c2 = input()
s = ""
for i in range(n):
    if i % 2 == 0:
        s += c1
    else:
        s += c2
print(s)