import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        total_time = end - start
        print(f"Total time to execute the function: {total_time}")
        return result
    return wrapper

@timer
def testing():
    time.sleep(3)

testing()