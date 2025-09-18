from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"calling : {func.__name__}")
        result =  func(*args,**kwargs)
        return result
    return wrapper


@log_activity
def brew_tea(type):
    print(f"brewing {type} chai")

brew_tea("Elaichi","ginger tea")    