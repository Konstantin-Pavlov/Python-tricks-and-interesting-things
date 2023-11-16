import re

text1 = "еда, беда, победа"
text2 = "Еда, беду, победа"
text3 = "Еда, беду, 5 победа"
text4 = "3Еда, 78беду, 4 555 победа"
text5 = "3Еда -4, 78беду12, 42 4 555 победа"
text6 = "3Еда -4, -78беду12, 42 4 -555 победа"
text7 = "-6453Еда, беду12, 42 4 -555 победа 6 654, fd"
text8 = "-6453ЕдF, беду12, 42 4 -555 поБеда 6 654, fd"
text9 = "0xf, 0xa, 0x5" # hexadecimal digits

match1 = re.findall(r"еда", text1)
match2 = re.findall(r"[Ее]д[ау]", text2)
match3 = re.findall(r"[0123456789]", text3)
match4 = re.findall(r"[0123456789]", text4)
match5 = re.findall(r"[0123456789][0123456789]", text5)  # same [0-9][0-9]
match6 = re.findall(r"[-0-9][\d]", text6)  # -0-9 <=> \d
match7 = re.findall(r"[^0-9]", text7)  # not numbers
match8 = re.findall(r"[а-я]", text8)  # only lowercase Cyrillic letters
match9 = re.findall(r"[а-яА-Я]", text8)  # all Cyrillic letters
match10 = re.findall(r"[а-яА-Я0-9]", text8)  # all Cyrillic letters and all numbers
match11 = re.findall(r"0x[\d]", text9)  # all Cyrillic letters and all numbers
match12 = re.findall(r"0x[\da-fA-F]", text9) 

print(match1)  # ['еда', 'еда', 'еда']
print(match2)  # ['Еда', 'еду', 'еда']
print(match3)  # ['5']
print(match4)  # ['3', '7', '8', '4', '5', '5', '5']
print(match5)  # ['78', '12', '42', '55']
print(match6)  # ['-4', '-7', '12', '42', '-5', '55']
print(match7)  # ['-', 'Е', 'д', 'а', ',', ' ', 'б', 'е', 'д', 'у', ',', ' ', ' ', ' ', '-', ' ', 'п', 'о', 'б', 'е', 'д', 'а', ' ', ' ', ',', ' ', 'f', 'd']
print(match8)  # ['д', 'б', 'е', 'д', 'у', 'п', 'о', 'е', 'д', 'а']
print(match9)  # ['Е', 'д', 'б', 'е', 'д', 'у', 'п', 'о', 'Б', 'е', 'д', 'а']
print(match10)  # ['6', '4', '5', '3', 'Е', 'д', 'б', 'е', 'д', 'у', '1', '2', '4', '2', '4', '5', '5', '5', 'п', 'о', 'Б', 'е', 'д', 'а', '6', '6', '5', '4']
print(match11) # ['0x5']
print(match12) # ['0xf', '0xa', '0x5']
