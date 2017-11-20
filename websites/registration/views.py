# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout, login as auth_login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
            if request.POST.get('is_popup_schedule', None):
                try:
                    if login_form.is_valid():
                        request.session['full_name'] = request.user.full_name
                        request.session['phone'] = request.user.phone
                        request.session['email'] = request.user.email
                        return JsonResponse({})
                        
                    return JsonResponse({"code": 400, 'errors': login_form.errors}, status=400)
                except Exception, e:
                    print "Error action login : ", e
                    return JsonResponse({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)
            else:
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
                messages.success(request, _('Register Account Successfully. Please Check Your Email and Active Account.'))
                return redirect(reverse('home'))
            else:
                # keep data of user input
                context = {}
                context['full_name'] = request.POST[
                    'full_name'] if 'full_name' in request.POST else None
                context['birth_date'] = request.POST[
                    'birth_date'] if 'birth_date' in request.POST else None
                context['address'] = request.POST[
                    'address'] if 'address' in request.POST else None
                context['personal_id'] = request.POST[
                    'personal_id'] if 'personal_id' in request.POST else None
                context['gender'] = request.POST[
                    'gender'] if 'gender' in request.POST else None
                context['city'] = request.POST[
                    'city'] if 'city' in request.POST else None
                context['district'] = request.POST[
                    'district'] if 'district' in request.POST else None
                context['phone'] = request.POST[
                    'phone'] if 'phone' in request.POST else None
                context['email'] = request.POST[
                    'email'] if 'email' in request.POST else None
                context['password1'] = request.POST[
                    'password1'] if 'password1' in request.POST else None
                context['password2'] = request.POST[
                    'password2'] if 'password2' in request.POST else None
                context['is_signup'] = True
                context['form'] = register_form
                return render(request, 'registration/signup.html', context)

        return render(request, 'registration/signup.html',
                      {'register_form': register_form, 'is_signup': True})
    except Exception, e:
        print "Error action register_user : %s" % e
        return HttpResponse(status=500)


def confirm_activation(request, activation_key):
    """ Action Confirm User Activation"""
    print 'Function Active User ', request.user.is_authenticated()
    try:
        User = get_user_model()
        result = {}
        # User is exist in system then confirm has account
        if request.user.is_authenticated():
            return render(request, 'registration/activation_confirm.html', {'has_account': True})

        # Check activation key is valid
        user_account = get_object_or_404(User,
                                         activation_key=activation_key)

        # User have confirm link before then return flag active
        if user_account.is_active:
            return render(request, 'registration/activation_confirm.html', {'active': True})

        # Check key expires
        if user_account.key_expires < timezone.now():
            return render(request, 'registration/activation_confirm.html', {'expired': True})

        # hanlder active account
        user_account.is_active = True
        user_account.save()
        user_account.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user_account)

        result['success'] = True
        return render(request, 'registration/activation_confirm.html', result)

    except Exception, e:
        print "Error action confirm_activation : %s" % e
        return HttpResponse(status=500)


@login_required(login_url='/login/')
def change_password(request):
    try:
        user = request.user
        form = ChangePasswordForm(user=user)
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST, user=user)

            if form.is_valid():
                form.save()
                messages.success(request, _('Update Password Successfully.'))
                return redirect(reverse('change_password'))

        return render(request, 'registration/change_password.html', {'form': form})
    except Exception, e:
        print "error", e
        return HttpResponse(status=500)


@login_required(login_url='/login/')
def update_profile(request):
    try:
        user = request.user
        # init form for case GET action
        user_form = UpdateUserForm(user=user)
        context = {'form': user_form, 'full_name': user.full_name, 'birth_date': user.birth_date,
                   'address': user.address, 'personal_id': user.personal_id, 'gender': user.gender,
                   'city': user.city, 'district': user.district, 'phone': user.phone, 'email': user.email}

        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, user=user)
            if user_form.is_valid():
                user_form.save()
                request.session['full_name'] = request.user.full_name
                request.session['phone'] = request.user.phone
                request.session['email'] = request.user.email
                messages.success(request, _('Update Profile Successfully.'))
                return redirect(reverse('profile'))
            else:
                # keep data of user input
                context['full_name'] = request.POST[
                    'full_name'] if 'full_name' in request.POST else None
                context['birth_date'] = request.POST[
                    'birth_date'] if 'birth_date' in request.POST else None
                context['address'] = request.POST[
                    'address'] if 'address' in request.POST else None
                context['personal_id'] = request.POST[
                    'personal_id'] if 'personal_id' in request.POST else None
                context['gender'] = request.POST[
                    'gender'] if 'gender' in request.POST else None
                context['city'] = request.POST[
                    'city'] if 'city' in request.POST else None
                context['district'] = request.POST[
                    'district'] if 'district' in request.POST else None
                context['phone'] = request.POST[
                    'phone'] if 'phone' in request.POST else None

                context['email'] = user.email
                context['form'] = user_form
                context['is_return'] = True

        return render(request, "registration/profile.html", context)
    except Exception, e:
        print "Error update_profile : ", e
        return HttpResponse(status=500)
