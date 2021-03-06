from django.shortcuts import render, redirect
from forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse


def logout(request):
    """ Action Login """
    try:
        auth_logout(request)
        return redirect(reverse('home'))
    except Exception, e:
        return HttpResponse(status=500)


def login(request):
    """ Action Login """
    try:
        # create flag is login using active tab in page html
        result = {'is_login': True}
        # user is active then redirect to home page
        if request.user.is_active:
            return redirect(reverse('home'))

        # validate LoginForm if valid then return homepage otherwise return
        # error
        if request.method == 'POST':
            login_form = LoginForm(request.POST, request=request)
            if login_form.is_valid():
                return redirect(reverse('home'))
            else:
                result['errors'] = login_form.errors

        return render(request, 'registration/signup.html', result)
    except Exception, e:
        return HttpResponse(status=500)


def register_user(request, **kwargs):
    """ Action Register User """
    # Init MetizSignupForm for get action
    try:
        register_form = MetizSignupForm(request=request)
        if request.method == 'POST':
            register_form = MetizSignupForm(request.POST, request=request)
            # check MetizSignupForm is valid then save user to db
            if register_form.is_valid():
                register_form.save()
                return redirect(reverse('home'))

        return render(request, 'registration/signup.html',
                      {'register_form': register_form, 'is_signup': True})
    except Exception, e:
        print "Error action register_user : %s" % e
        return HttpResponse(status=500)


def confirm_activation(request, activation_key):
    """ Action Confirm User Activation"""
    print 'Function Active User ', request.user.is_authenticated()
    try:
        result = {}
        # User is exist in system then confirm has account
        if request.user.is_authenticated():
            return render(request, 'registration/confirm.html', {'has_account': True})

        # Check activation key is valid
        user_account = get_object_or_404(DonorHubUser,
                                         activation_key=activation_key)

        # User have confirm link before then return flag active
        if user_account.is_active:
            return render(request, 'registration/confirm.html', {'active': True})

        # Check key expires
        if user_account.key_expires < timezone.now():
            return render(request, 'registration/confirm.html', {'expired': True})

        # hanlder active account
        user_account.is_active = True
        user_account.save()
        user_account.backend = 'django.contrib.auth.backends.ModelBackend'
        login_sys(request, user_account)

        result['success'] = True
        return render(request, 'websites/registration/confirm.html', result)

    except Exception, e:
        print "Error action confirm_activation : %s" % e
        return HttpResponse(status=500)
