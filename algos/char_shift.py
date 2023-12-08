# https://stepik.org/lesson/611485/step/15?unit=606807

def  shift_letter(char, shift):
    "Функция сдвигает символ letter на shift позиций"
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))


print(shift_letter('b', 2) )   #=> 'd'
print(shift_letter('d', 1) )   #=> 'e'
print(shift_letter('z', 1) )   #=> 'a'
print(shift_letter('d', -2))   # => 'b'

print(shift_letter('d', 26))   # => 'd'
print(shift_letter('b', -3))   # => 'y'