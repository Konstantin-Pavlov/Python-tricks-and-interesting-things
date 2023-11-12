'''

Sample Input 1:
7
8 5 3 1 4 7 9
Sample Output 1:
1 3 4 5 7 8 9
9

Sample Input 2:
3
9 8 -4
Sample Output 2:
-4 8 9
3

Sample Input 3:
7
7 13 -18 10 -14 4 -6

'''


n = int(input())
nums = list(map(int, input().split()))
swaps = 0

for i in range(n):
    swapped = False  # flag - if not swapped there's no point to continue inner for - useless runs
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            swaps += 1
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
    if not swapped:
        break
    
print(*nums)
print(swaps)