'''
Sample Input 1:
[]
Sample Output 1:
YES

Sample Input 2:
[(])
Sample Output 2:
NO

Sample Input 3:
{[]}()
Sample Output 3:
YES
'''

line = input()

for _ in range (len(line) // 2):
    line = line.replace("()", '')
    line = line.replace("[]", '')
    line = line.replace("{}", '')

print("NO" if len(line) else "YES")


###


brackets = input()
stack = []
is_good = True
for bracket in brackets:
    if bracket in '({[':
        stack.append(bracket)
    elif bracket in ')}]':
        if not stack:
            is_good = False 
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and bracket == ')':
            continue
        if open_bracket == '{' and bracket == '}':
            continue
        if open_bracket == '[' and bracket == ']':
            continue
        is_good = False 
        break
print("YES" if is_good and len(stack) == 0 else "NO")



###

brackets = input()
stack = []
is_good = True
for bracket in brackets:
    if bracket in '({[':
        stack.append(bracket)
    elif bracket in ')}]':
        if not stack:
            is_good = False 
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and bracket == ')':
            continue
        if open_bracket == '{' and bracket == '}':
            continue
        if open_bracket == '[' and bracket == ']':
            continue
        is_good = False 
        break
print("YES" if is_good and len(stack) == 0 else "NO")