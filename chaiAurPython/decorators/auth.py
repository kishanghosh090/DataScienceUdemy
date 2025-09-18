from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied : admin only")
        else:
            return func(user_role)            
    return wrapper            


@require_admin
def access_tea(role):
    print("Access granted to tea world")

access_tea("user")
access_tea("admin")