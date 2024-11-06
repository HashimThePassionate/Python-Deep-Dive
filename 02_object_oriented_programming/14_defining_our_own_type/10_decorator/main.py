import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"⏳ Starting '{func.__name__}'")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ '{func.__name__}' finished in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def compute_squares(n):
    return [i**2 for i in range(n)]

# Usage
compute_squares(1000000)
