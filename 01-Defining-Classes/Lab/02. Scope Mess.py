x = "global"

def outer():
    global x
    x = "local"

    def inner():
        global x
        x = "nonlocal"
        print("inner:", x)
        return x


    def change_global():
        global x
        x = "global: changed!"
        return x

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
