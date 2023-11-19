# https://stepik.org/lesson/372102/step/1?unit=359656

from random import randint
n = 3
m = 4
matrix = [[randint(1,10) for j in range(m)] for i in range(n)]
for current_row in matrix:
    print(current_row)
    
print('-'*30)

squares = [num**2 for row in matrix for num in row]
print(squares)