from django.shortcuts import render, redirect
from forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout


def logout(request):
    auth_logout(request)
    return redirect(reverse('home'))


def login(request):
    result = {'is_login': True}

    if request.user.is_active:
        return redirect(reverse('home'))

    if request.method == 'POST':
        login_form = LoginForm(request.POST, request=request)
        if login_form.is_valid():
            return redirect(reverse('home'))
        else:
            result['errors'] = login_form.errors

    return render(request, 'registration/signup.html', result)


def register_user(request, **kwargs):
    register_form = MetizSignupForm(request=request)
    print "Call Action register "
    if request.method == 'POST':

        register_form = MetizSignupForm(request.POST, request=request)
        print 'form is valid', register_form.errors.as_json()
        if register_form.is_valid():
            register_form.save()
            return redirect(reverse('home'))

    return render(request, 'registration/signup.html',
                  {'register_form': register_form, 'is_signup': True})


def confirm_activation(request, activation_key):
    print 'Function Active User ', request.user.is_authenticated()
    try:
        result = {}
        if request.user.is_authenticated():
            return render(request, 'registration/confirm.html', {'has_account': True})
        user_account = get_object_or_404(DonorHubUser,
                                         activation_key=activation_key)
        if user_account.is_active:
            return render(request, 'registration/confirm.html', {'active': True})

        if user_account.key_expires < timezone.now():
            return render(request, 'registration/confirm.html', {'expired': True})

        user_account.is_active = True
        user_account.save()
        user_account.backend = 'django.contrib.auth.backends.ModelBackend'
        login_sys(request, user_account)

        result['success'] = True
        return render(request, 'websites/registration/confirm.html', result)

    except Exception, e:
        raise e
