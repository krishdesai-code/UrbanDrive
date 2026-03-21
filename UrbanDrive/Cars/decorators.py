from django.shortcuts import redirect
from functools import wraps

def session_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if 'id' exists in session
        if not request.session.get('id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper