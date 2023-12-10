# print(*[i for i in range(0, 501, 5)], sep="\n")

# from random import choices

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random_numbers = choices(numbers, k=4)

# from pprint import pprint

# #a = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]
# colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
# sizes = ['S', 'M', 'L', 'XL', 'XLL']

# print([(color, size) for color in colors for size in sizes ])


def get_word_indices(strings: list[str]) -> dict:
    d = {}
    for line_ind, line in enumerate(strings):
        for word in line.split():
            d[word.lower()] = d.get(word.lower(), []) + [line_ind]
    return d


assert get_word_indices(["This is a string", "test String", "test", "string"]) == {
    "this": [0],
    "is": [0],
    "a": [0],
    "string": [0, 1, 3],
    "test": [1, 2],
}

assert get_word_indices(["Look at my horse", "my horse", "is amazing"]) == {
    "look": [0],
    "at": [0],
    "my": [0, 1],
    "horse": [0, 1],
    "is": [2],
    "amazing": [2],
}

assert get_word_indices([]) == {}

assert get_word_indices(["Avada Kedavra", "avada kedavra", "AVADA KEDAVRA"]) == {
    "avada": [0, 1, 2],
    "kedavra": [0, 1, 2],
}


# impo turtle as t
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
