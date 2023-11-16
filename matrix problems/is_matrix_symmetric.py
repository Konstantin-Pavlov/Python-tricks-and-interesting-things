'''

Sample Input 1:
3
0 1 2
1 5 3
2 3 4
Sample Output 1:
Yes

Sample Input 2:
3
0 0 0
0 0 0
1 0 0
Sample Output 2:
No

Sample Input 3:
5
0 0 0 0 0
0 0 0 0 0
1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Sample Output 3:
No

Sample Input 4:
5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Sample Output 4:
Yes

'''

# not optimazed
n = int(input())   

matrix = []   
main_diagonal_sum = 0
symmetry = True

for _ in range(n):    
    temp = [int(a) for a in input().split()]
    matrix.append(temp)


for i in range(n):
    for j in range(n): 
        if matrix[i][j] != matrix[j][i]:
            symmetry = False

print('Yes' if symmetry else 'No') 


#############################

# to one dimention
n = int(input())
s = [input().split() for i in range(n)]
s1 = [[s[j][i] for j in range(n)] for i in range(n)]
print('Yes' if s == s1 else 'No')



