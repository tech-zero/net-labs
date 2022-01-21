
'''
In this demo, we will define and create a decorator which is going 
to allow us to measure performance of our functions execution.
The 'perf_counter() function' will return the value (in fractional 
seconds) of a performance counter.
'''
from time import perf_counter 


def performance_test(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        finish = perf_counter()
        performance = finish - start
        print(f"Execution time: {performance}\n")
    return wrapper


@performance_test
def print_some_number(num):
    for i in range(0, num):
        print(i)


print_some_number(500)
#print_some_number(3245)
