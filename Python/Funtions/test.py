def outer():
    print("outer function is called")
    def inner():
        print("inner is called")
    print("outer is calling inner")
    return inner
a=outer()
a()
a()
a()
a()