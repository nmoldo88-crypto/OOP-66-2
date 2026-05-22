# decorators and  venv


def simple_decorator(func):
    def wrapper():
        print("before commit!!")
        func()
        print("after commit!!")
    return wrapper

@simple_decorator
def say_hello():
    print("hello world")
say_hello()