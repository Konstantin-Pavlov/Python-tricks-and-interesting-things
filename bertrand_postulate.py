"""

https://stepik.org/lesson/296963/step/5?unit=278691

Постулат Бертрана (теорема Бертрана-Чебышева, теорема Чебышева) гласит, что для любого n > 1 найдется простое число p в интервале n < p < 2n. Такая гипотеза была выдвинута в 1845 году французским математиком Джозефем Бертраном (проверившим ее до n=3000000) и доказана в 1850 году Пафнутием Чебышевым. Рамануджан в 1920 году нашел более простое доказательство, а Эрдеш в 1932 – еще более простое.

Ваша задача состоит в том, чтобы решить несколько более общую задачу – а именно по числу n найти количество простых чисел p из интервала n < p < 2n.

Напомним, что число называется простым, если оно делится только само на себя и на единицу.

Входные данные
Программа принимает на вход целое число n (2 ≤ n ≤ 50000).

Sample Input 1:
2
Sample Output 1:
1

Sample Input 2:
4
Sample Output 2:
2

Sample Input 3:
239
Sample Output 3:
39

Sample Input 4:
3000
Sample Output 4:
353

"""


def primes(n):
    """
    Оптимизация
    В цикле можно попробовать исключить четные i и начать перебор с 3 с шагом 2
    Надо добавить ещё if, чтобы цикл работал только если  n > 1 и n нечетное, так же если n = 2, но в этом случае,       хотя мы и попадём в else, цикл не запустится, т.к. начинается с 3 и тогда (наверное) он переходит на else где       возвращает True
    """
    if n < 2 or n % 2 == 0 and n != 2:
        return False
    else:
        for i in range(3, int(n / 2) + 1, 2):
            if n % i == 0:
                return False
        else:
            return True


def primes_in_a_range(a, b):
    total_primes = 0
    for i in range(a, b):
        if primes(i):
            total_primes += 1
    return total_primes


number = int(input())
print(primes_in_a_range(number + 1, number * 2))
