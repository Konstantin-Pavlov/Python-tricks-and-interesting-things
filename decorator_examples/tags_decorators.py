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

@table
@header
def hello(name, surname, age):
    print(f"hello {name} {surname}, age of {age}")

hello("Jon", "Dow", 42)