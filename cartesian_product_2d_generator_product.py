# https://stepik.org/lesson/372102/step/2?unit=359656

"""

Здесь мы берем каждый цвет и сочетаем его с каждым размером

colors = ['red', 'green']
sizes = ['S', 'M', 'L']


[('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L')]

"""


colors = ["White", "Blue", "Yellow", "Purple", "Black", "Green"]
sizes = ["S", "M", "L", "XL", "XLL"]

print([(color, size) for color in colors for size in sizes])


print()


from itertools import product as decart

print(list(decart(colors, sizes)))


print()


print(list(__import__('itertools').product(colors, sizes)))
