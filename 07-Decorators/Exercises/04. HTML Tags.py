def tags(tag):
    def decorator(function):
        def wrapper(*param):
           return f"<{tag}>{function(*param)}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
