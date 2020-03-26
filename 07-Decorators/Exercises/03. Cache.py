def cache(func):
    def wrapper(n):
        wrapper.log[n] = func(n)
        return func(n)
    wrapper.log = {}
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(3)
print(fibonacci.log)
