# Begin23. Даны переменные A, B, C. 
# Изменить их значения, переместив содержимое A в B, B — в C, C — в A, и вывести новые значения переменных A, B, C.
a = float(input())
b = float(input())
c = float(input())

temp = a
a = b
b = c
c = temp

print(a)
print(b)
print(c)