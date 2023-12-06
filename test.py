# print(*[i for i in range(0, 501, 5)], sep="\n")

# from random import choices

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random_numbers = choices(numbers, k=4)

# from pprint import pprint

# #a = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]
# colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
# sizes = ['S', 'M', 'L', 'XL', 'XLL']

# print([(color, size) for color in colors for size in sizes ])

def count_AGTC(dna):
    d = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    for el in dna:
        d[el] += 1
    print(d)
    return tuple(d.values())

# код ниже не стоит удалять, он нужен для проверки
print( count_AGTC('AGGTC')) # (1, 2, 1, 1)
print( count_AGTC('AAAATTT')  ) # (4, 0, 3, 0)
print( count_AGTC('AGTTTTT')  ) # (1, 1, 5, 0)
print( count_AGTC('CCT')   )  # (0, 0, 1, 2) 



# import turtle as t
# from random import randint

# t.Screen().colormode(255)
# t.Screen().setup(400, 400)
# t.speed(0)
# t.bgcolor((0, 0, 0))
# for i in range(333):
#     t.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     t.left(70)  # randint(40, 90)
#     t.forward(i)
# t.done()


# from turtle import *

# color('cyan', 'purple')   # Первый цвет: линия, второй цве: заливка.
# width(1)   # Толщина линии.
# speed(100)   # Скорость рисования.
# begin_fill()   # Начало заливки.
# while True:   # Бесконечный цикл.
#     forward(750)   # Движение по прямой на указанное количество пикселей.
#     left(145)   # Поворот налево на указанное количество градусов.
#     if abs(pos()) < 1:   # Если ресующая стрелка вернулась на изначальную позицию:
#         break   # Принудительно завершить цикл.
# end_fill()   # Конец заливки.
# done()   # Предотвращает закрытие холста.