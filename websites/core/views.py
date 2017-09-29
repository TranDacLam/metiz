# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import *


def custom_404(request):
	return render(request, 'websites/errors/404.html', {}, status=404)

def custom_500(request):
	return render(request, 'websites/errors/500.html', {}, status=500)

def showing(request):
	
	data_showing = Movie.objects.filter(release_date__lte=datetime.now())
	return render(request, 'websites/showing.html', {'data_showing':data_showing})

def comingsoon(request):	

	data = Movie.objects.filter(release_date__gte=datetime.now())
	return render(request, 'websites/coming_soon.html', {'data':data })
	
def film_detail(request, id):	
	
	film_detail = Movie.objects.get(pk=id)
	return render(request, 'websites/film_detail.html', {'film_detail': film_detail})
