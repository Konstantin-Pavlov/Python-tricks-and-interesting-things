'''
https://stepik.org/lesson/372111/step/10?unit=359665

Премия Оскар
Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках)

Ваша задача написать программу, которая находит информацию, кто из актеров получил наибольшее и наименьшее количество статуэток

Входные данные
Программа принимает на вход в первой строке натуральное число n - количество вручаемых сегодня наград. 
И затем в n следующих строках вводятся имена актеров - победителей.

Выходные данные
Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток 
и через запятую их количество. Гарантируется, что всегда будет только один человек, 
набравший наибольшее и наименьшее количество статуэток.

Sample Input:
6
Леонардо Ди Каприо
Джонни Депп
Леонардо Ди Каприо
Леонардо Ди Каприо
Джонни Депп
Мэтт Деймон
Sample Output:
Леонардо Ди Каприо, 3
Мэтт Деймон, 1


'''


actors = {}
for i in range(int(input())):
    actor = input()
    
    actors[actor] = actors.get(actor, 0) + 1

max_oscar_actor = max(actors, key=actors.get) # type: ignore
min_oscar_actor = min(actors, key=actors.get) # type: ignore
print(f"{max_oscar_actor}, {actors[max_oscar_actor]}")
print(f"{min_oscar_actor}, {actors[min_oscar_actor]}")



'''
from collections import Counter
dct = Counter([input() for i in '_' * int(input())])
mx, mn = max(dct, key=dct.get), min(dct, key=dct.get)
print('%s, %d\n%s, %d' % (mx, dct[mx], mn, dct[mn]))
'''