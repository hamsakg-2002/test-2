def validate_numbers(func):
    def wrapper(a, b):
        if a < 0 or b < 0:
            print("Only positive numbers allowed")
            return
        return func(a, b)
    return wrapper


@validate_numbers
def add(a, b):
    print(a + b)


add(10, 20)
add(-1, 5)