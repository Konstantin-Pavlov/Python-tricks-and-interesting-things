d1 = {"India": "Delhi", "Canada": "Ottawa", "United States": "Washington D. C."}

d2 = {"France": "Paris", "Malaysia": "Kuala Lumpur"}

capitals = d1 | d2
print(capitals)


# {'India': 'Delhi', 'Canada': 'Ottawa', 'United States': 'Washington D. C.', 'France': 'Paris', 'Malaysia': 'Kuala Lumpur'}


d = {1: "one", 2: "two", 3: "three"}
w = {4: "four", 5: "five"}
d.update(w)
print(d)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

lang = {"eng": "Английский", "ru": "Русский"}
other = {"esp": "Spanish", "ru": "Rus"}
lang.update(other)
print(lang)  # {'eng': 'Английский', 'ru': 'Rus', 'esp': 'Spanish'}


# another way

a = {"name": "Andrey"}
b = {"age": 31}
c = {**a, **b}
