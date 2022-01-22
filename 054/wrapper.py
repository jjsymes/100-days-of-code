def call_twice(function):
    def wrapper_function():
        function()
        function()
    return wrapper_function

def print_border(string):
    def function_with_border(function):
        def wrapper(*args, **kwargs):
            border = string * 20
            print(border)
            result = function(*args, **kwargs)
            print(border)
            return result
        return wrapper
    return function_with_border


@print_border("@")
@call_twice
def hello_world():
    print("Hello World")

hello_world()
