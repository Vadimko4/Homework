from typing import Any

from time import time

def log(filename: str = '') -> Any:
    def decorator(func):
        def wraper(*args, **kwargs):
            start_time = time()
            if filename:
                with open(filename, "a", encoding='utf-8') as file:
                    file.write(f"{func.__name__} {start_time = }\n")
                    try:
                        result = func(*args, **kwargs)
                        end_time = time()
                        file.write(f"{func.__name__} ok\n")
                        file.write(f"{func.__name__} {end_time = }\n\n")
                        return result
                    except Exception as e:
                        end_time = time()
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                        file.write(f"{func.__name__} {end_time = }\n\n")
                        raise Exception(e)
            else:
                print(f"\n{func.__name__} {start_time = }")
                try:
                    result = func(*args, **kwargs)
                    end_time = time()
                    print(f"{func.__name__} OK")
                    print(f"{func.__name__} {end_time = }\n")
                    return result
                except Exception as e:
                    end_time = time()
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    print(f"{func.__name__} {end_time = }\n")
                    raise Exception(e)
        return wraper
    return decorator