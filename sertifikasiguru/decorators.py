from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def decoadmin(func):
    def decorated(request, *args, **kwargs):
        # print (request.session['id_user'])
        if 'admin' not in request.session:
            return redirect('adminmasuk')
        else:
            return func(request, *args, **kwargs)
    # decorated.__doc__ = func.__doc__
    # decorated.__name__ = func.__name__
    return decorated


def decoclient(func):
    def decorated(request, *args, **kwargs):
        # print (request.session['id_user'])
        if 'client' not in request.session:
            return redirect('masuk')
        else:
            return func(request, *args, **kwargs)
    # decorated.__doc__ = func.__doc__
    # decorated.__name__ = func.__name__
    return decorated

