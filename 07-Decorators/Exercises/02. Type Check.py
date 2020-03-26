def type_check(instance_type):
    def decorator(function):
        def wrapper(param):
            if isinstance(param, instance_type):
                return function(param)
            else:
                return f"Bad Type"
        return wrapper
    return decorator
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
