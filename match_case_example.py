'''
https://stepik.org/lesson/988826/step/1?unit=996311
https://proproprogs.ru/python_base/python3-konstrukciya-matchcase-pervoe-znakomstvo -> далее более сложные примеры
'''

cmd = "top"
commands = ("TOP", "BOTTOM", "RIGHT", "LEFT")
match cmd:
    case str() as command if command.upper() in commands:
        print(f"Команда {command.lower()}")
    case _:
        print("Неверная команда")

def get_data_ver_1(value):
    match value:        
        case bool() as command:
            return command
        case str() as command:
            return command
        case int() as command:
            return command
        case float() as command:
            return command
    
    return None

def get_data_ver_2(value):
    match value:
        case bool():
            return None
        case int() | float() | str() as data:
            return data
    return None

def get_data_ver_3(value):
    print(type(value))
    match value:        
        case bool() as command:
            return command
        case str() as command:
            return command
        case int() as command if command > 0:
            return command
        case float() as command if -100 <= command <= 100:
            return command
    
    return None


print(get_data_ver_3(-56.4))



# cmd = ("Балакирев С.М.", "Python", 2000.78)
cmd = ("Балакирев С.М.", "Python", 2000.78, 2020)

match cmd:
    case (author, title, price) :
        print(f"Книга: {author}, {title}, {price}")
    case (_, author, title, price, year):
        print(f"Книга: {author}, {title}, {price}, {year}")
    case (author, title, price, year):
        print(f"Книга: {author}, {title}, {price}, {year}")
    case _:  # wildcard
        print("непонятный формат данных")


###########################################################################################
# https://stepik.org/lesson/988843/step/5?unit=996328
def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': bool(access), 'data': [date, *_]}: 
            return access, date
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

print(parse_json(json_data))



###########################################################################################
# https://stepik.org/lesson/988843/step/6?unit=996328

def parse_json1(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': True, 'data': [_, {'login': str(login), 'email': str(email)}, _, *_]}:
            return login, email
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}