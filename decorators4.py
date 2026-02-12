def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Error:", e)
    return wrapper


@exception_handler
def calculate(a, b):
    return a / b


print(calculate(10, 0))
