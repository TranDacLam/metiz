from django.shortcuts import redirect
from django.core.urlresolvers import reverse

"""
	Check user booking info is exist
"""
def check_user_booking_exist(f):
    def wrap(request, *args, **kwargs):
            # this check the session if phone key exist, if not it will redirect to login page
            if 'phone' not in request.session.keys():
                return redirect(reverse('login'))
            return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap
