# List28. Дан список из N строк и буква. Генератором вывести строки, начинающиеся с этой буквы (первый символ строки)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
letter = input()
b = [s for s in a if s.startswith(letter)]
print(b)