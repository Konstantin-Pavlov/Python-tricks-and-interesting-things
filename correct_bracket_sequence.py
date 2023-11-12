'''
Sample Input 1:
(())
Sample Output 1:
YES

Sample Input 2:
(()
Sample Output 2:
NO

Sample Input 3:
())
Sample Output 3:
NO

Sample Input 4:
()()
Sample Output 4:
YES

Sample Input 5:
))((
Sample Output 5:
NO

Sample Input 6:
()())
Sample Output 6:
NO

Sample Input 7:
)(
Sample Output 7:
NO
'''

t = input()
while t.count('()'):
    t = t.replace('()', '')
print(["NO", "YES"][len(t) == 0])