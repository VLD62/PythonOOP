def logged(function):
    def decorator(*args):
        func_arguments = args
        result = function(*args)
        return (f"you called {function.__name__}{func_arguments}\nit returned {result}")
    return decorator


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
