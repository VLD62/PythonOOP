
def vowel_filter(function):
    the_vowels = ["a","e","i","o","u"]
    def wrapper():
        return [x for x in function() if x.lower() in the_vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
