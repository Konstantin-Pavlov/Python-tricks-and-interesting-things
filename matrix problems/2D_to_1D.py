'''

[j for i in list for j in i]
j - элемент
i - подсписок
list - список подсписков.


есть двумерный список vector. 
при помощи генератора-списка сделать на основании vector 
линейный(одномерный ) список и вывести его

'''

vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print([element for sub_vector in vector for element in sub_vector])

