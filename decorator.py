# Python Decorators education with 
# YouTube video: https://youtu.be/r7Dtus7N4pI


def some_func(indside_func):
    def wrapper(*args):
        print("Start")
        indside_func(*args)
        print("End")

    return wrapper


@some_func
def func_print(text):
    print(text)

# func_print = some_func(func_print)('lol')

func_print("Kek")