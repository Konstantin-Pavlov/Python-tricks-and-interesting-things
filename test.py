# print(*[i for i in range(0, 501, 5)], sep="\n")

# from random import choices

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random_numbers = choices(numbers, k=4)

from pprint import pprint

#a = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]
colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']

print([(color, size) for color in colors for size in sizes ])