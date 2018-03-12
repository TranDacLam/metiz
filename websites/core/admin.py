# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from models import *
from django import forms
import custom_models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from core import widgets
from hitcount.models import HitCount, HitCountMixin
from hitcount.admin import *

""" Start hide hitcount group on admin site """
admin.site.unregister(Hit)
admin.site.unregister(HitCount)
admin.site.unregister(BlacklistUserAgent)
admin.site.unregister(BlacklistIP)
""" End hide hitcount group on admin site """

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
            raise forms.ValidationError(_("Passwords don't match"))
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


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        release_date = self.cleaned_data.get('release_date')
        if end_date and end_date < release_date:
            raise forms.ValidationError(
                _("Ngày kết thúc phải lớn hơn ngày khởi chiếu."))
        return end_date


class MovieAdmin(admin.ModelAdmin):
    form = MovieForm
    # inlines = [GenreInline, ]
    filter_horizontal = ('genre', )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(Movie, MovieAdmin)


class NewOfferForm(forms.ModelForm):

    class Meta:
        model = NewOffer
        fields = '__all__'

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        apply_date = self.cleaned_data.get('apply_date')
        if end_date and end_date < apply_date:
            raise forms.ValidationError(
                _("Ngày kết thúc phải lớn hơn ngày áp dụng."))
        return end_date

        
class NewOfferAdmin(admin.ModelAdmin):
    form = NewOfferForm
    list_display = ('name', 'apply_date', 'modified')
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


class CommentForm(forms.ModelForm):
    date_post = forms.SplitDateTimeField(
        widget=widgets.CustomAdminSplitDateTime())

    class Meta:
        model = Comment
        fields = '__all__'


class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
    pass
admin.site.register(Comment, CommentAdmin)


# class PostForm(forms.ModelForm):
#     key_query = forms.CharField(max_length=200, required=False)
#     class Meta:
#         model = Post
#         fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    # form = PostForm

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('key_query',)
        return self.readonly_fields

    pass
admin.site.register(Post, PostAdmin)


class SlideShowAdmin(admin.ModelAdmin):
    pass
admin.site.register(SlideShow, SlideShowAdmin)


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()},
    }
    pass
admin.site.register(Blog, BlogAdmin)