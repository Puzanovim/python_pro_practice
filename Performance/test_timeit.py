from timeit import timeit

setup_a = """
set_a = set(range(1000000))
"""
statement_a = """
result_a = 10550 in set_a
"""
result_a = timeit(setup=setup_a, stmt=statement_a)

setup_b = """
list_b = list(range(1000000))
"""
statement_b = """
result_b = 10550 in list_b
"""
result_b = timeit(setup=setup_b, stmt=statement_b)
print(f"result A: {result_a}\nresult B: {result_b}")
