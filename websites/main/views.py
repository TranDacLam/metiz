# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from core.models import *
from datetime import *


def custom_404(request):
	return render(request, 'websites/errors/404.html', {}, status=404)

def custom_500(request):
	return render(request, 'websites/errors/500.html', {}, status=500)

