# import random
from timeit import timeit
#
#
# def sort_expensive():
#     the_list = random.sample(range(1000000), 1000)
#     the_list.sort()
#
#
# def sort_cheap():
#     the_list = random.sample(range(1000), 10)
#     the_list.sort()
#
#
# if __name__ == '__main__':
#     setup_expensive = """
#     import random
#
#     def sort_expensive():
#         the_list = random.sample(range(1000000), 1000)
#         the_list.sort()
#     """
#     setup_cheap = """
#     import random
#
#     def sort_cheap():
#         the_list = random.sample(range(1000), 10)
#         the_list.sort()
#     """
#     statement_expensive = """sort_expensive()"""
#     statement_cheap = """
#     for _ in range(1000):
#         sort_cheap()
#     """
#     time_expensive = timeit(setup=setup_expensive, stmt=statement_expensive)
#     time_cheap = timeit(setup=setup_cheap, stmt=statement_cheap)
#     print(f"expensive: {time_expensive}\ncheap: {time_cheap}")
#     sort_expensive()
#     for _ in range(1000):
#         sort_cheap()


setup_expensive = """
import random

def sort_expensive():
    the_list = random.sample(range(1000), 1000)
    the_list.sort()
"""
setup_cheap = """
import random

def sort_cheap():
    the_list = random.sample(range(1), 10)
    the_list.sort()
"""
statement_expensive = "sort_expensive()"
statement_cheap = """
for _ in range(1000):
    sort_cheap()
"""
print("time EX start")
time_expensive = timeit(setup=setup_expensive, stmt=statement_expensive)
print("time EX finish")
print("time CH start")
time_cheap = timeit(setup=setup_cheap, stmt=statement_cheap)
print("time CH finish")
print(f"expensive: {time_expensive}\ncheap: {time_cheap}")
