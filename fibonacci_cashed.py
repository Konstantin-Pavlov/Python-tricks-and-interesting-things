def fibonacci_get(n, cache={}):
    if n <= 1:
        return n
    return cache.get(n, cache.setdefault(n, fibonacci(n-1) + fibonacci(n-2)))

def fibonacci(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

print(fibonacci(70))
print(fibonacci_get(70))