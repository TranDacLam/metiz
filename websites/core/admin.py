# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from django import forms
import custom_models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = custom_models.User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = custom_models.User
        fields = ('email', 'password', 'birth_date', 'phone', 'full_name', 'gender', 'personal_id',
                  'city', 'district', 'address', 'is_active', 'is_staff', 'is_superuser',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'phone', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'birth_date', 'phone',
                                      'gender', 'personal_id', 'city', 'district', 'address',)}),
        ('Permissions', {'fields': ('is_staff',
                                    'is_superuser', 'is_active', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'phone', )
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...

admin.site.register(custom_models.User, UserAdmin)


class RatedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rated, RatedAdmin)


class GenreAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(Genre, GenreAdmin)


class MovieTypeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(MovieType, MovieTypeAdmin)


class MovieAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(Movie, MovieAdmin)


class NewOfferAdmin(admin.ModelAdmin):
    exclude = ('movies',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(NewOffer, NewOfferAdmin)


class BannerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(Banner, BannerAdmin)


class CenimaTechnologyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(CenimaTechnology, CenimaTechnologyAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('key_query',)
        return self.readonly_fields
        
    pass
admin.site.register(Post, PostAdmin)


class SlideShowAdmin(admin.ModelAdmin):
    pass
admin.site.register(SlideShow, SlideShowAdmin)

