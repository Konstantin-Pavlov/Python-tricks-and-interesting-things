'''

https://stepik.org/lesson/372095/step/3?unit=359649

Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию merge_sort, 
которая будет принимать исходный список и возвращать новый отсортированный в порядке неубывания список.

Также для реализации функции merge_sort вам понадобится реализовать функцию merge_two_list. 
Функция merge_two_list должна принимать два отсортиванных по неубыванию списка, 
сливать их в один большой список также отсортированный по неубыванию (задача Слияние списков ) и возвращать его.

Ваша задача написать только определение функций merge_sort и merge_two_list, 
при этом нельзя пользоваться встроенными сортировками в Python

Sample Input:
7
6 2 19 5 10 7 11
Sample Output:
2 5 6 7 10 11 19

'''


# функция merge_two_list должна объединить два списка
def merge_two_list(a, b):
    new_list = []
    while a and b:
        new_list += [a.pop(0) if a < b else b.pop(0)]
        if not a:
            new_list.extend(b)
        if not b:
            new_list.extend(a)       
    return new_list

# функция merge_sort должна выполнить сортировку
def merge_sort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    a, b = l[:mid], l[mid:]
    return merge_two_list(merge_sort(a), merge_sort(b))

