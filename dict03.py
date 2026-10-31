# Dict3. Построить словарь из N пар. Дан ключ K: вывести значение через get с default 0 одной строкой
n = int(input())
d = read_dict(n)
k = input()
print(d.get(k, 0))