from operator import add, sub, truediv, mul


def calculate(x: float, y: float, operation: str = "a") -> None:
    def addition():
        print(x + y)

    def subtraction():
        print(x - y)

    def division():
        if not y:
            print("На ноль делить нельзя!")
            return
        print(x / y)

    def multiplication():
        print(x * y)

    operation_dict = {
        "a": addition,
        "s": subtraction,
        "d": division,
        "m": multiplication,
    }

    selected_operation = operation_dict.get(operation)
    if selected_operation:
        operation_dict[operation]()
    else:
        print("Ошибка. Данной операции не существует")
    

calculate(2, 5) # Печатает 7.0
calculate(2.2, 15, 'a') # Печатает 17.2
calculate(22, 15, 's') # Печатает 7.0
calculate(2, 3.2, 'm') # Печатает 6.4
calculate(10, 0.4, 'd') # Печатает 25.0




# def calculate(x: float, y: float, operation: str='a') -> None:
#     opers = {'a': add,
#              's': sub,
#              'd': truediv,
#              'm': mul}
#     try:
#         print(opers[operation](x, y))
#     except KeyError:
#         print('Ошибка. Данной операции не существует')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')