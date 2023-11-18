import re

# квантификаторы 

'''
{m, n}
m => min number of matches
n => max number of matches

***

{m} => exactly m times
{m,} => >= m
{,n} => <= n

{m,}? => minor mode

{0, } => >= 0 повторений; 
{1, } => >= 1 повторений

аналог {0, 1} => ?
аналог {0,} => *?
аналог {1,} => +?
'''

text = "Google, Gooogle, Goooooogle"

match0 = re.findall(r"o{2,5}", text)
match1 = re.findall(r"o{2,5}?", text) # ? - minor mode
match2 = re.findall(r"Go{2,}gle", text) # more than 2 'o'
match3 = re.findall(r"Go{,4}gle", text) # less than 4 'o'


# print(match0) # ['oo', 'ooo', 'ooooo']
# print(match1) # ['oo', 'oo', 'oo', 'oo', 'oo']
# print(match2) # ['Google', 'Gooogle', 'Goooooogle']
# print(match3) # ['Google', 'Gooogle']


###################################################

phone_number = "89126547984"

phone_number_match = re.findall(r"8\d{10}", phone_number) # сначала идёт 8, потом 10 подряд идущих цифр

# print(phone_number_match) # ['89126547984']

###################################################

text = "стеклянный, стекляный"
match = re.findall(r"стеклянн?ый", text) # <=> {0, 1}
# print(match)  # ['стеклянный', 'стекляный']

###################################################

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
# \w - символы от 1 до сколько найдется, \s - могут быть пробелы (* - от 0 и более), потом =
# после = могут быть пробелы (* - от 0 и более); [^;]+ - все символы кроме ;
match0 = re.findall(r"\w+\s*=\s*[^;]+", text) 
match1 = re.findall(r"(\w+)\s*=\s*([^;]+)", text) 
# print(match0) # ['author=Пушкин А.С.', 'title = Евгений Онегин', 'price =200', 'year= 2001']
# print(match1) # [('author', 'Пушкин А.С.'), ('title', 'Евгений Онегин'), ('price', '200'), ('year', '2001')]


###################################################

# minor quantifiers

text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
text1 = "<p>Картинка  <img alt='картинка'      src='bg.jpg'> в тексте</p>"
text3 = "<p>Картинка  <img> в тексте</p>"

# <img.*> - здесь .* будет искать максимальную последовательность заканчивающееся > (жадный (мажорный) квантификатор)
match0 = re.findall(r"<img.*>", text)

# <img.*?> - здесь ? будет искать минимальную последовательность заканчивающееся > (минорный квантификатор)
match1 = re.findall(r"<img.*?>", text)

# [^>] - жадный (мажорный) квантификатор, но будет искать до > потому что она не входит в последовательность
match2 = re.findall(r"<img[^>]*>", text)

match3 = re.findall(r"<img[^>]*>", text1)

# более корректный вариант - \s - могут быть пробелы, минорный до src; 
match4 = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text1)

match5 = re.findall(r"<img[^>]*>", text3)
match6 = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text3)

print(match0) # ["<img src='bg.jpg'> в тексте</p>"]
print(match1) # ["<img src='bg.jpg'>"]
print(match2) # ["<img src='bg.jpg'>"]
print(match3) # ["<img alt='картинка'      src='bg.jpg'>"]
print(match4) # ["<img alt='картинка'      src='bg.jpg'>"]
print(match5) # ['<img>'] => wrong
print(match6) # [] ok

