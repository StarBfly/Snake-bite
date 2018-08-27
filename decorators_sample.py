from time import time
import time as t


def wrapper(func):
    def _wrapper(*args, **kwargs):
        begin_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(f"Time of execution: {end_time - begin_time}")
    return _wrapper

@wrapper
def func(x):
    t.sleep(10)
    return [x * i for i in range(1000)]

print(func(3))