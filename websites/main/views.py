# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def custom_404(request):
    return render(request, 'websites/errors/404.html', {}, status=404)

def custom_500(request):
    return render(request, 'websites/errors/500.html', {}, status=500)

def home(request):
    print "############ "
    return render(request, 'websites/home.html', {})