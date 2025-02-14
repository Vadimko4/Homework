from typing import Any

def log(filename: str = '') -> Any:
    def decorator(func):
        def wraper(*args, **kwargs):
            if filename:
                with open(filename, "a") as file:
                    try:
                        result = func(args, kwargs)
                        file.write(f"{func.__name__} ok\n")
                        return result
                    except Exception as e:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                        raise Exception(e)
            else:
                try:
                    result = func(args, kwargs)
                    print(f"{func.__name__} OK")
                    return result
                except Exception as e:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    raise Exception(e)
        return wraper
    return decorator