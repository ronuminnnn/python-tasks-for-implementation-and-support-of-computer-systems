# Dict15. Построить словари из N и M пар. 
# Добавить в первый пары второго без update: только ключи, которых нет; совпавшие ключи считать проигнорированными. 
# Вывести размер и число проигнорированных
n = int(input())
first = read_dict(n)
m = int(input())
second = read_dict(m)
ignored = 0
for key, value in second.items():
    if key in first:
        ignored += 1
    else:
        first[key] = value
print(len(first))
print(ignored)