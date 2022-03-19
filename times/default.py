import time

def example_func():
    print('example_func')

start = time.time()
example_func()
process_time = time.time() - start

print(process_time)
