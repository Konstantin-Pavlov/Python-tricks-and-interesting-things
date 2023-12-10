"""

Sample Input 1:
Argentine Peso
Sample Output 1:
118362.205708

Sample Input 2:
Рубль
Sample Output 2:
Нет данных по Рубль

Sample Input 3:
US Dollar
Sample Output 3:
1127.074905

"""


currencies = {
    "Argentine Peso": 118362.205708,
    "Australian Dollar": 1586.232315,
    "Bahraini Dinar": 423.780164,
    "Botswana Pula": 13168.450636,
    "Brazilian Real": 5954.781483,
    "British Pound": 834.954104,
    "Bruneian Dollar": 1520.451015,
    "Bulgarian Lev": 1955.83,
    "Canadian Dollar": 1430.54405,
    "Chilean Peso": 898463.818465,
    "Chinese Yuan Renminbi": 7171.445692,
    "Colombian Peso": 4447741.922165,
    "Croatian Kuna": 7527.744707,
    "Czech Koruna": 24313.797041,
    "Danish Krone": 7440.613895,
    "Emirati Dirham": 4139.182587,
    "Hong Kong Dollar": 8786.255952,
    "Hungarian Forint": 355958.035747,
    "Icelandic Krona": 143603.932438,
    "Indian Rupee": 84241.767127,
    "Indonesian Rupiah": 16187150.010697,
    "Iranian Rial": 47534006.535121,
    "Israeli Shekel": 3569.191411,
    "Japanese Yen": 129149.364679,
    "Kazakhstani Tenge": 489292.515538,
    "Kuwaiti Dinar": 340.959682,
    "Libyan Dinar": 5196.539901,
    "Malaysian Ringgit": 4717.485104,
    "Mauritian Rupee": 49212.933037,
    "Mexican Peso": 23130.471272,
    "Nepalese Rupee": 134850.008728,
    "New Zealand Dollar": 1703.649473,
    "Norwegian Krone": 9953.078431,
    "Omani Rial": 433.360301,
    "Pakistani Rupee": 198900.635421,
    "Philippine Peso": 57574.278782,
    "Polish Zloty": 4579.273862,
    "Qatari Riyal": 4102.552652,
    "Romanian New Leu": 4946.638369,
    "Russian Ruble": 86197.012666,
    "Saudi Arabian Riyal": 4226.530892,
    "Singapore Dollar": 1520.451015,
    "South African Rand": 17159.831129,
    "South Korean Won": 1355490.097163,
    "Sri Lankan Rupee": 228245.645722,
    "Swedish Krona": 10439.125427,
    "Swiss Franc": 1037.792217,
    "Taiwan New Dollar": 31334.286611,
    "Thai Baht": 37436.518169,
    "Trinidadian Dollar": 7636.35428,
    "Turkish Lira": 15078.75981,
    "US Dollar": 1127.074905,
    "Venezuelan Bolivar": 511082584.868731,
}

print(currencies.get((key := input()), f"Нет данных по {key}"))

###########################################################################

money = input()
text = f'Нет данных по {money}'
print(currencies.get(money, text))

print()

# синтаксис
dna = 'AGGTC'
d = {}
for el in dna:
    # если нет ключа el , по умолчанию будет 0, если есть прибавится 1  
    d[el] = d.get(el, 0) + 1
print(d) # {'A': 1, 'G': 2, 'T': 1, 'C': 1}


###########################################################################

# https://stepik.org/lesson/296973/step/14?thread=solutions&unit=278701

'''

В этой задаче вам необходимо создать функцию get_word_indices, 
которая принимает список строк и возвращает словарь, 
где ключи - это уникальные слова из списка строк в нижнем регистре, 
а значения - это списки индексов строк, в которых эти слова встречаются.

Регистр букв не учитывается поэтому слова «String» и «STRING» считаются одинаковыми
Нужно написать только определение функции get_word_indices 

'''



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
