def pass_fail(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print(" RESULT: PASS")
            return "PASS"

        except Exception as e:
            print(" RESULT: FAIL")
            print("Reason:", e)
            return "FAIL"

    return wrapper
@pass_fail
def check_boot_log(file):
    with open(file) as f:
        if "ERROR" in f.read():
            raise Exception("Boot error detected")

