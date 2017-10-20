# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def logout(request):
    """ Action Login """
    try:
        auth_logout(request)
        messages.success(request, 'Bạn đã đăng xuất thành công.')
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
                messages.success(request, 'Bạn đã đăng nhập thành công.')
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
                messages.success(request, 'Bạn đã đăng ký thành công.')
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


@login_required(login_url='/admin/login/')
def change_password(request):
    try:
        user = request.user
        form = ChangePasswordForm()
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)

            if form.is_valid():
                newpassword = form.cleaned_data['new_password']
                old_password = form.cleaned_data['old_password']
                valid = user.check_password(old_password)
                if not valid:
                    return render(request, 'registration/change_password.html')
                user.set_password(newpassword)
                user.save()
                return redirect(reverse('home'))

            else:
                return render(request, 'registration/change_password.html', {'error': 'You have entered wrong old password', 'form': form})
        else:
            form = ChangePasswordForm()
        content = RequestContext(request, {'form': form})
        return render(request, 'registration/change_password.html')
    except Exception, e:
        print "error", e
        return HttpResponse(status=500)


@login_required(login_url='/admin/login/')
def update_profile(request):
    try:
        user = request.user
        # init form for case GET action
        user_form = UpdateUserForm()
        context = {'form': user_form, 'username': user.username, 'birth_date': user.birth_date,
                   'address': user.address, 'personal_id': user.personal_id, 'gender': user.gender,
                   'city': user.city, 'district': user.district, 'email': user.email}

        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return redirect(reverse('home'))
            else:
                # keep data of user input
                context['username'] = request.POST['username']
                context['birth_date'] = request.POST['birth_date']
                context['address'] = request.POST['address']
                context['personal_id'] = request.POST['personal_id']
                context['gender'] = request.POST['gender']
                context['city'] = request.POST['city']
                context['district'] = request.POST['district']
                context['email'] = user.email
                context['form'] = user_form

        return render(request, "registration/profile.html", context)
    except Exception, e:
        print "Error update_profile : ", e
        return HttpResponse(status=500)
