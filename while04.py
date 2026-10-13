# While4. Дано целое число N (> 0). Если оно является степенью числа 3, то вывести TRUE, если не является — вывести FALSE.
N = int(input())
while N % 3 == 0:
    n//=3
if n == 1:
    print("True")
else:
    print("False")