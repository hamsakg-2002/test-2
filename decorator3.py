import time

def retry(count=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retry {i+1}/{count}")
                    time.sleep(1)
            print(" All retries failed")
        return wrapper
    return decorator


@retry(count=3)
def test():
    print("Running function...")
    raise Exception("Failed")



