"""

https://stepik.org/lesson/296967/step/7?thread=solutions&unit=278695

Sample Input 1:
1 2 3
Sample Output 1:
{1: {2: 3}}

Sample Input 2:
45 45 66 21 94 62 50 13 96
Sample Output 2:
{45: {45: {66: {21: {94: {62: {50: {13: 96}}}}}}}}

Sample Input 3:
7 38 20 49 87 69
Sample Output 3:
{7: {38: {20: {49: {87: 69}}}}}

Sample Input 4:
49 67 36
Sample Output 4:
{49: {67: 36}}

"""

def dic_rec(d, lst):
    if lst:
        new_dict = {}
        new_dict.update(d)
        d.clear()
        d[lst.pop()] = new_dict 
        dic_rec(d, lst)

nums = list(map(int, input().split()))
d = {}
d[nums.pop()] = nums.pop()

dic_rec(d, nums)
print(d)



###################################################


a = list(map(int, input().split()))
d = a[-1]
for i in a[-2::-1]:
    d = {i: d}
print(d)


###################################################


li = [int(i) for i in input().split()]
d = li.pop()
while li:
    d = {li.pop(): d}
print(d)


###################################################


def nested_dict(lst):
    return {lst[0]: nested_dict(lst[1:])} if len(lst) > 2 else dict([lst])

lst = list(map(int, input().split()))    
print(nested_dict(lst)) 
