# Python Decorators education with 
# YouTube video: https://youtu.be/r7Dtus7N4pI
 
def decofunc(inside_func):
    def wrapper(*args):
        print("Started")
        inside_func(*args)
        print("Ended")
    
    return wrapper


def func(*args):
    print(*args)


func = decofunc(func)
func("Oh", "what", "a", "wonderful", "world")