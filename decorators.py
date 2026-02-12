def validate_positive(func):
    def wrapper(num):
        if num <= 0:
            print("Invalid number")
            return
        return func(num)
    return wrapper


@validate_positive
def square(n):
    print(n * n)


square(5)
square(-3)
