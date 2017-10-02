# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import *
from django.db.models import Avg


def custom_404(request):
	return render(request, 'websites/errors/404.html', {}, status=404)

def custom_500(request):
	return render(request, 'websites/errors/500.html', {}, status=500)

def showing(request):
	
	data_showing = Movie.objects.filter(release_date__lte=datetime.now()).order_by('priority', 'release_date')
	return render(request, 'websites/showing.html', {'data_showing':data_showing})

def comingsoon(request):	

	data = Movie.objects.filter(release_date__gte=datetime.now()).order_by('priority', 'release_date')
	return render(request, 'websites/coming_soon.html', {'data':data })
	
def film_detail(request, id):	
	
	film_detail = Movie.objects.get(pk=id)
	comments = Comment.objects.filter(movie=id)
	rating__avg = Comment.objects.filter(movie=id).aggregate(rating=(Avg('rating')))
	return render(request, 'websites/film_detail.html', {'film_detail': film_detail,'comments': comments,'rating__avg':rating__avg})


def news(request):
	news=NewOffer.objects.all().order_by('priority', 'apply_date')
	return render(request, 'websites/news.html', {'news': news})

def new_detail(request, id):
	new=NewOffer.objects.get(pk=id)
	return render(request, 'websites/new_detail.html', {'new': new})

def getCinemaTechnologyByName(request, name):
	allTechnology= CenimaTechnology.objects.all()
	technology = allTechnology.get(name = name)
	return render(request, 'websites/cinema_technology.html', {'technology': technology, 'allTechnology':allTechnology})



def home(request):
	data={'banner': ["assets/websites/images/banner-cgv/a.jpg","assets/websites/images/banner-cgv/b.jpg","assets/websites/images/banner-cgv/c.jpg","assets/websites/images/banner-cgv/d.jpg"],
		'movie': ["assets/websites/images/movie-selection/movie1.png","assets/websites/images/movie-selection/movie2.jpg","assets/websites/images/movie-selection/movie3.jpg","assets/websites/images/movie-selection/movie4.jpg","assets/websites/images/movie-selection/movie5.jpg"],
		'event':["assets/websites/images/events/event1.jpg","assets/websites/images/events/event2.jpg","assets/websites/images/events/event3.jpg","assets/websites/images/events/event4.jpg","assets/websites/images/events/event6.png","assets/websites/images/events/event7.jpg"],
		'tv_cgv':["assets/websites/images/thanhvien-cgv/tv1.jpg","assets/websites/images/thanhvien-cgv/tv2.jpg","assets/websites/images/thanhvien-cgv/tv3.jpg","assets/websites/images/thanhvien-cgv/tv4.jpg","assets/websites/images/thanhvien-cgv/tv5.jpg"],
		'movie_soon':["assets/websites/images/american_made_240x355.png","assets/websites/images/american_made_240x355.png","assets/websites/images/american_made_240x355.png","assets/websites/images/american_made_240x355.png","assets/websites/images/american_made_240x355.png"]
	}
	# banner on home page
	result = {}	
	banners = Banner.objects.filter(is_show=True).order_by('position')
	banner_position = {}
	for item in banners:
		banner_position[item.position] = item
	result["banners"] = banner_position
	
	return render(request, 'websites/home.html', {'data': data, 'result':result})



