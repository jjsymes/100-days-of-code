# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f"Log: running {function.__name__}")
        function(*args)
    return wrapper_function

# Use the decorator 👇

@logging_decorator
def do_something(thing):
    print(f"Doing {thing}")


do_something("code")