from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.utils.html import format_html


class CustomAdminSplitDateTime(forms.SplitDateTimeWidget):
    """
    A SplitDateTime Widget that has some admin-specific styling.
    """

    def __init__(self, attrs=None):
        widgets = [admin_widgets.AdminDateWidget,
                   admin_widgets.AdminTimeWidget]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def format_output(self, rendered_widgets):
        return format_html('<p class="datetime">{}<br />{}</p>',
                           rendered_widgets[0],
                           rendered_widgets[1])
