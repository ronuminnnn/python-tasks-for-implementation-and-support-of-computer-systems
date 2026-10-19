# List30. Дан список из N строк. Генератором вывести список длин строк и суммарную длину всех строк
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
lengths = [len(s) for s in a]
print(lengths)
print(sum(lengths))