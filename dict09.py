# Dict9. Построить словари из N и M пар. Слить второй в первый через update. 
# Вывести размер результата и значение ключа, который был в обоих словарях (такой ключ гарантированно есть)
n = int(input())
first = read_dict(n)
m = int(input())
second = read_dict(m)
common = None
for key in second:
    if key in first:
        common = key
first.update(second)
print(len(first))
print(first[common])