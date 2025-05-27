
# I alrady have 'login_required' decorator, if user not logged in.
# but what if i want, if user logged in, so not go login or signin page 
# hope you know well what is requirements, and thats why we make that coustom decorator !!! 


from django.shortcuts import redirect
from functools import wraps
from django.contrib.auth import REDIRECT_FIELD_NAME

def redirect_if_authenticated(redirect_to=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user is *not* logged in, redirecting
    to the specified page if necessary.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                # Redirect authenticated users to the specified URL or the default
                redirect_to_value = redirect_to or 'your_default_redirect_url' # Replace with your default URL
                return redirect(redirect_to_value)
            else:
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# from django.contrib.auth.decorators import login_required
# @login_required(login_url="/security/login/")
def redirect_if_superuser(redirect_to=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user is superuser, if not so redirecting
    to the specified page if necessary.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            print("redirect_if_superuser")
            if not request.user.is_superuser:
                # Redirect authenticated users to the specified URL or the default, if he is not superuser
                redirect_to_value = redirect_to or 'your_default_redirect_url' # Replace with your default URL
                return redirect(redirect_to_value)
            else:
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
