#!/usr/bin/env python3
# import collections

def log_and_count(key=None, counts=None):
    if counts is None:
       raise TypeError("Missing argument count")
    def outside(function):
        def inside(*args, **kwargs):
            print(f"called {function.__name__} with {args} and {kwargs}")
            ret = function(*args, **kwargs)
            if key is None:
                counts[function.__name__] += 1
            else:
                counts[key] += 1
            return ret
        return inside
    return outside

# my_counter = collections.Counter()

# @log_and_count(key = 'basic functions', counts = my_counter)
# def f1(a, b=2):
#     return a ** b

# @log_and_count(key = 'basic functions', counts = my_counter)
# def f2(a, b=3):
#     return a ** 2 + b

# @log_and_count(counts = my_counter)
# def f3(a, b=5):
#     return a ** 3 - b

# f1(2)
# f2(2, b=4)
# f1(a=2, b=4)
# f2(4)
# f2(5)
# f3(5)
# f3(5,4)

# print(my_counter)