import random
import time


def an_expensive_function():
    execution_time = random.random() / 100
    time.sleep(execution_time)


if __name__ == '__main__':
    """
    start with command: python -m cProfile --sort cumtime Performance\cpu_profiling.py
    ncall: count call
    tottime: clear time in this method (without child calls)
    percall: average time in this call
    cumtime: total time in this method include child calls
    """
    for _ in range(1000):
        an_expensive_function()
