from typing import Any


def log(filename: str = '') -> Any:
    """
    Декоратор автоматически логирует результаты выполнения функции, или возникшие ошибки.
    Принимает необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль):
    если filename задан, логи записываются в указанный файл.
    если не задан, логи выводятся в консоль.
    Логирование включает:
    имя функции и  результат выполнения при успешной операции, либо
    имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке;
    """
    def decorator(func):
        def wraper(*args, **kwargs):
            #start_time = time()
            if filename:
                with open(filename, "a", encoding='utf-8') as file:
                    #file.write(f"{func.__name__} {start_time = }\n")
                    try:
                        result = func(*args, **kwargs)
                        #end_time = time()
                        file.write(f"{func.__name__} ok\n")
                        #file.write(f"{func.__name__} {end_time = }\n\n")
                        return result
                    except Exception as e:
                        #end_time = time()
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                        #file.write(f"{func.__name__} {end_time = }\n\n")
                        raise Exception(e)
            else:
                #print(f"\n{func.__name__} {start_time = }")
                try:
                    result = func(*args, **kwargs)
                    #end_time = time()
                    print(f"{func.__name__} ok")
                    #print(f"{func.__name__} {end_time = }\n")
                    return result
                except Exception as e:
                    #end_time = time()
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    #print(f"{func.__name__} {end_time = }\n")
                    raise Exception(e)
        return wraper
    return decorator
