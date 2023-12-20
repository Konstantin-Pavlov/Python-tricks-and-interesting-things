def multiply(*args):
    return __import__("functools").reduce(
        lambda a, b: a * b, args, 1
    )  # 1  - default agrument


def multiply_with_prod(*args):
    return __import__("math").prod(args)


def multiply_with_recursion(*args):
    if not args:
        return 1
    return args[0] * multiply_with_recursion(*args[1:])


assert multiply(1, 2, 3) == 6
assert multiply(1, 3) == 3
assert multiply(2) == 2
assert multiply() == 1

assert multiply_with_prod(1, 2, 3) == 6
assert multiply_with_prod(1, 3) == 3
assert multiply_with_prod(2) == 2
assert multiply_with_prod() == 1

assert multiply_with_recursion(1, 2, 3) == 6
assert multiply_with_recursion(1, 3) == 3
assert multiply_with_recursion(2) == 2
assert multiply_with_recursion() == 1
