# minitask 8

def deprecated(func):
    def inner(*args, **kwargs):
        print(f"Call to deprecated function: {func.__name__}")
        print(f"with args: {args}")
        print(f"with kwargs: {kwargs}")
        x = args[0]
        y = kwargs["y"]
        print(f"returning: {func(x, y)}") 
    return inner

@deprecated
def some_old_function(x, y):
    return x + y

some_old_function(1,y=2)

# should print:
# Call to deprecated function: some_old_function
# with args: (1,)
# with kwargs: {'y': 2}
# returning: 3 
