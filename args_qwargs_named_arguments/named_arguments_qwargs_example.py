'''

https://stepik.org/lesson/372076/step/16?thread=solutions&unit=359630

Напишите функцию create_actor, которая принимает произвольное количество именованных аргументов и возвращает словарь с характеристиками актера. Если функции create_actor не передавать никаких аргументов, то она должна возвращать базовый словарь с ключами name, surname, age. Вот так он выглядит:

create_actor() -> {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }
Если передавать именованные параметры, которые отсутствуют в базовом словаре, они дополняются к этому словарю 

create_actor(height=190, movies=['Дедпул', 'Главный герой']) => {
    'name': 'Райан',
    'surname': 'Рейнольдс',
    'age': 46,
    'height': 190,
    'movies': ['Дедпул', 'Главный герой']
}
Если передавать именованные параметры, которые совпадают с ключами базового словаря, то значения в словаре должны заменяться переданными значениями:

create_actor(name='Jack', age=20) -> {
        'name': 'Jack',
        'surname': 'Рейнольдс',
        'age': 20,
    }

'''

def create_actor(name='Райан', surname='Рейнольдс', age=46,**qwargs):
    # return {'name': name, 'surname': surname, 'age': age, **kwargs}
    # return {'name': 'Райан','surname': 'Рейнольдс','age': 46,} | kwargs
    d =   {'name': name, 'surname': surname, 'age': age}
    d.update(qwargs)
    return d


# print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))

assert create_actor() == {
    'name': 'Райан',
    'surname': 'Рейнольдс',
    'age': 46, }
assert create_actor(height=190, movies=['Дедпул', 'Главный герой']) == {
    'name': 'Райан',
    'surname': 'Рейнольдс',
    'age': 46,
    'height': 190,
    'movies': ['Дедпул', 'Главный герой']}
assert create_actor(name='Jack', age=20) == {
    'name': 'Jack',
    'surname': 'Рейнольдс',
    'age': 20, }