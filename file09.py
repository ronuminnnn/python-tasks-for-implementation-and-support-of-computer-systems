# File9 Даны имена двух файлов: один существует и непуст (не обязательно первый), другой отсутствует. 
# Создать отсутствующий и записать в него конечный и начальный элементы существующего
import os
a = input()
b = input()
if os.path.exists(a):
    src, dst = a, b
else:
    src, dst = b, a
with open(src, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    f.write(str(nums[-1]) + "\n")
    f.write(str(nums[0]) + "\n")