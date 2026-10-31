# Dict7. Построить словарь из N пар. Вывести ключ с наибольшим значением (перебор с кандидатом; значения различны)
n = int(input())
d = read_dict(n)
best = None
for key in d:
    if best is None or d[key] > d[best]:
        best = key
print(best)