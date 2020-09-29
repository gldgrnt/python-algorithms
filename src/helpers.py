# Helper function to measure the execution time of functions
from timeit import default_timer as timer 

def execution_time(func, args):
    # Measure time to run func
    start = timer()
    value = func(args)
    stop = timer()

    time = stop - start
    return print(f'Value: {value} in {time}s')