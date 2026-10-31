# Dict12. Построить словарь из N пар с различными значениями. 
# Построить обращённый словарь: значение ключ. 
# Вывести его пары в порядке добавления исходного
n = int(input())
d = read_dict(n)
inverted = {}
for key, value in d.items():
    inverted[value] = key
for value, key in inverted.items():
    print(f"{value}: {key}")