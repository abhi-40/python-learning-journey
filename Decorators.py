def decorator(func):
    def wrapper():
        print("About to execute a function")
        func()
        print("Exectued function")
    return wrapper

@decorator
def say_hello():
    print("Hello")
say_hello()