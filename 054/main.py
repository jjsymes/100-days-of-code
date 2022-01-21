import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def function_with_timer():
        function()
        new_time = time.time()
        diff = new_time - current_time
        print(f"Function execution time: {diff}s")
    return function_with_timer


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
