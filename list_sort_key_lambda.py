# doesn't work for some reason
def f(x):
    return x % 10, x % 2, x


# ok
def custom_sort(x):
    if x % 10 == 0:
        return (0, x)
    elif x % 2 == 0:
        return (1, x)
    else:
        return (2, x)


numbers = [72, 4, 39, 100, 200, 5, 28, 123, 44]

# ok
sorted_numbers = (
    sorted(filter(lambda x: x % 10 == 0, numbers))
    + sorted(filter(lambda x: x % 2 == 0 and x % 10 != 0, numbers))
    + sorted(filter(lambda x: x % 2 != 0 and x % 10 != 0, numbers))
)

print(sorted_numbers)

numbers.sort(key=custom_sort)
print(numbers)
