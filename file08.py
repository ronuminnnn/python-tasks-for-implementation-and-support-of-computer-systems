# File8 Даны имена двух файлов: первый существует и непуст, второй отсутствует. 
# Создать второй и записать в него первый и последний элементы первого
src = input()
dst = input()
with open(src, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    f.write(str(nums[0]) + "\n")
    f.write(str(nums[-1]) + "\n")