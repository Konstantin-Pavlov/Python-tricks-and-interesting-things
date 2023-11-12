'''
https://en.wikipedia.org/wiki/Insertion_sort
https://stepik.org/lesson/296963/step/8?unit=278691
https://pythontutor.com/render.html#mode=display


Sample Input 1:
6
5 4 2 15 6 6
Sample Output 1:
2 4 5 6 6 15

Sample Input 2:
5
11 2 8 1 5
Sample Output 2:
1 2 5 8 11

'''

n = int(input())
numbers = [int(a) for a in input().split()]
for i in range(1, n):
    current_num = numbers[i]
    j = i
    while j > 0 and numbers[j - 1] > current_num:
        numbers[j] = numbers[j - 1]
        j -= 1
    numbers[j] = current_num
print(*numbers)


#########################################################################

# charGPT version
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Пример использования
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Отсортированный массив:", my_list)