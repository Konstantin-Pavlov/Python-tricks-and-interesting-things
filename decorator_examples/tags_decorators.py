def text_decor(func):
    def inner(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Goodbye!")
    return inner

def header(func):
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")
    return inner

def table(func):
    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    return inner

@text_decor
@table
@header
def hello(name, surname, age):
    print(f"hello {name} {surname}, age of {age}")

hello("Jon", "Dow", 42)