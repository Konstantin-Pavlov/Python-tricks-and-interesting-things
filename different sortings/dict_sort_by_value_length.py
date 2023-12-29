"""
https://stepik.org/lesson/372111/step/14?thread=solutions&unit=359665

Входные данные
Ваша задача вывести в порядке уменьшения популярности 3 строки вида:
"Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
На склонение давайте не будем обращать внимание в этой задаче.

Гарантируется, что количество уникальных комментаторов у всех наших героев разное. Могут быть ситуации, когда у героя нету ни единого комментатора, в таком случае все равно нужно выводить информацию о нем.

Sample Input 1:
Дили: navalny
Дили: realdonaldtrump
Били: navalny
Вили: realdonaldtrump
Вили: realdonaldtrump
Били: joebiden
Дили: joebiden
конец
Sample Output 1:
Количество уникальных комментаторов у Дили - 3
Количество уникальных комментаторов у Били - 2
Количество уникальных комментаторов у Вили - 1

Sample Input 2:
Дили: aaaa
Дили: aaaa
Били: aaaa
Дили: aaaa
Били: aaa
конец
Sample Output 2:
Количество уникальных комментаторов у Били - 2
Количество уникальных комментаторов у Дили - 1
Количество уникальных комментаторов у Вили - 0


"""


unique_subscribers = {"Дили": set(), "Вили": set(), "Били": set()}

lines = [line.split(": ") for line in iter(input, "конец")]
[unique_subscribers[line[0]].add(line[1]) for line in lines]
[
    print(f"Количество уникальных комментаторов у {k} - {len(v)}")
    for k, v in sorted(unique_subscribers.items(), key=lambda x: -len(x[1]))
]