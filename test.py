# print(*[i for i in range(0, 501, 5)], sep="\n")

# from random import choices

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random_numbers = choices(numbers, k=4)

# from pprint import pprint

# #a = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]
# colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
# sizes = ['S', 'M', 'L', 'XL', 'XLL']

# print([(color, size) for color in colors for size in sizes ])

def caesar_cipher(line, shift):
    for letter in line:   
        if ord(letter) - shift < 97:
            print(chr(ord(letter) - shift + 26), end="")
        else:
            print(chr(ord(letter) - shift), end="")

def  shift_letter(char, shift):
    "Функция сдвигает символ letter на shift позиций"
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))


# print(caesar_cipher('leave out all the rest', -1)) #=> 'kdzud nts zkk sgd qdrs'
# print(caesar_cipher('one more light', 3)) #=> 'rqh pruh oljkw'

print(shift_letter('b', 2) )#=> 'd'
print(shift_letter('d', 1) )#=> 'e'
print(shift_letter('z', 1) )#=> 'a'
print(shift_letter('d', -2))# => 'b'
print(shift_letter('d', 26))# => 'd'
print(shift_letter('b', -3))# => 'y'

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