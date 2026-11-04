# File1. Дана строка S. Если S — допустимое имя файла, создать пустой файл с этим именем и вывести True, иначе False
s = input()
try:
    with open(s, "a", encoding="utf-8") as f:
        pass
    print(True)
except OSError:
    print(False)