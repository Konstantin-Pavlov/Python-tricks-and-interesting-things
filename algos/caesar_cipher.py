
"""
Шифр цезаря
Этот шифр брал каждую букву исходной фразы и смещал ее на значение ключа. 
В пределах кодирования одной фразы значение сдвига всегда постоянно.
"""


def shift_letter(char, shift):
    "Функция сдвигает символ letter на shift позиций"
    if not char.isalpha():
        return char
    if char.isupper():
        return chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
    else:
        return chr((ord(char) - ord("a") + shift) % 26 + ord("a"))


def caesar_cipher(line, shift):
    "Шифр цезаря"
    result = ""
    for letter in line:
        result += shift_letter(letter, shift)
    return result


print(caesar_cipher("leave out all the rest", -1))  # => 'kdzud nts zkk sgd qdrs'
print(caesar_cipher("one more light", 3))  # => 'rqh pruh oljkw