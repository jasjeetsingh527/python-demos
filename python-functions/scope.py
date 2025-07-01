# Scope - What variable do i gave access to?
a = 1


def confusion():
    a = 5
    return a


print(a)  # => returns 1
print(confusion())  # => returns 5


# Global
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())


# nonlocal

x = ""


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outter:", x)


outer()

print(x)
