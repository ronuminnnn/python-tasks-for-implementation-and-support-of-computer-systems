# Dict8. Построить словарь из N пар и число V. Вывести True, если V встречается среди значений, и False иначе
n = int(input())
d = read_dict(n)
v = int(input())
print(v in d.values())