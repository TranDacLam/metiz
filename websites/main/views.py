# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def custom_404(request):
	return render(request, 'websites/errors/404.html', {}, status=404)

def custom_500(request):
	return render(request, 'websites/errors/500.html', {}, status=500)

def home(request):
	data={'banner': ["assets/websites/images/banner-cgv/a.jpg","assets/websites/images/banner-cgv/b.jpg","assets/websites/images/banner-cgv/c.jpg","assets/websites/images/banner-cgv/d.jpg"],
		'movie': ["assets/websites/images/movie-selection/movie1.png","assets/websites/images/movie-selection/movie2.jpg","assets/websites/images/movie-selection/movie3.jpg","assets/websites/images/movie-selection/movie5.jpg"],
		'event':["assets/websites/images/events/event1.jpg","assets/websites/images/events/event2.jpg","assets/websites/images/events/event3.jpg","assets/websites/images/events/event4.jpg","assets/websites/images/events/event6.png","assets/websites/images/events/event7.jpg"],
		'tv_cgv':["assets/websites/images/thanhvien-cgv/tv1.jpg","assets/websites/images/thanhvien-cgv/tv2.jpg","assets/websites/images/thanhvien-cgv/tv3.jpg","assets/websites/images/thanhvien-cgv/tv4.jpg","assets/websites/images/thanhvien-cgv/tv5.jpg"]
	}
	
	return render(request, 'websites/home.html', {'data': data})

def comingsoon(request):
	data=[{'img':"/assets/websites/images/movie-selection/movie1.png"}, {'img':"/assets/websites/images/movie-selection/movie1.png"}, {'img': "/assets/websites/images/movie-selection/movie1.png"},{'img': "/assets/websites/images/movie-selection/movie1.png"}	,{'img': "/assets/websites/images/movie-selection/movie1.png"}]	
	return render(request, 'websites/coming_soon.html', {'data':data })

def cinox(request):
	
	return render(request, 'websites/cinox.html', {})

def gift_card(request):
	
	return render(request, 'websites/gift_card.html', {})

def membership(request):
	
	return render(request, 'websites/membership.html', {})

def movie_voucher(request):
	
	return render(request, 'websites/movie_voucher.html', {})

def account_create(request):
	
	return render(request, 'websites/account_create.html', {})

def account_login(request):
	
	return render(request, 'websites/account_login.html', {})

def showing(request):	
	data=[{'img':"/assets/websites/images/movie-selection/movie1.png",'tc':"c18", 'rating':1},{'img':"/assets/websites/images/movie-selection/movie1.png"	,'tc': 'c16','rating':2},{'img': "/assets/websites/images/movie-selection/movie1.png",'tc': "p", 'rating':3}	,{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':4}	,{'img': "/assets/websites/images/movie-selection/movie1.png",'tc': "p", 'rating':5}]	
	return render(request, 'websites/showing.html', {'data':data})

def arthouse(request):	
	data=[{'img':"/assets/websites/images/movie-selection/movie1.png",'tc':"c18", 'rating':1},{'img':"/assets/websites/images/movie-selection/movie1.png"	,'tc': 'c16','rating':2},{'img': "/assets/websites/images/movie-selection/movie1.png",'tc': "p", 'rating':3}	,{'img': "/assets/websites/images/movie-selection/movie1.png",'tc': "p", 'rating':4}]	
	return render(request, 'websites/arthouse.html', {'data': data})


