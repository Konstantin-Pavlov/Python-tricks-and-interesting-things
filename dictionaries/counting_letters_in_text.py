from pprint import pprint
s = "123 Catch up on today’s global news 321"
d = {}
for i in s:
     if i.isalpha():
        d[i] = d.get(i, 0) + 1
pprint(d)
for letter, count in d.items():
    print(letter, count)