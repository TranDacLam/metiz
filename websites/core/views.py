# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import *
from django.db.models import Avg, Sum, Count


def custom_404(request):
    return render(request, 'websites/errors/404.html', {}, status=404)


def custom_500(request):
    return render(request, 'websites/errors/500.html', {}, status=500)


def showing(request):
    try:
        # get data movie showing
        data_showing = Movie.objects.filter(
            release_date__lte=datetime.now()).order_by('priority', 'release_date')
        return render(request, 'websites/showing.html', {'data_showing': data_showing})
    except Exception, e:
        print "Error: ", e

def comingsoon(request):
    try:
        # get data moving comingsoon
        data = Movie.objects.filter(release_date__gte=datetime.now()).order_by(
            'priority', 'release_date')
        return render(request, 'websites/coming_soon.html', {'data': data})
    except Exception, e:
        print "Error: ", e


def film_detail(request, id):
	try:
	    # get film detail by id
	    film_detail = Movie.objects.get(pk=id)
	    # filter comments of film detail by movie_id
	    comments = Comment.objects.filter(movie=id)
	    # average rating for film detail
	    rating__avg = comments.aggregate(rating=(Avg('rating')))
	    # count sum rating in comments
	    rating__sum = comments.aggregate(Sum('rating')).get('rating__sum')

	    dic = []
	    for i in range(1, 6):
	        # lay tong so sao cung loai (1 sao, 2 sao,...5 sao) trong danh gia
	        count = comments.filter(rating=i).aggregate(
	            Sum('rating')).get('rating__sum')
	        # dua tong so sao tung loai vao mang
	        dic.append(count)
	    return render(request, 'websites/film_detail.html', {'dic': dic, 'count': count, 'rating__sum': rating__sum, 'film_detail': film_detail, 'comments': comments, 'rating__avg': rating__avg})
	except Movie.ObjectDoesNotExist:
		print "Page not found !"
	except Exception, e:
		print "Error: ", e

def news(request):
    try:
        # get news order by priority and apply_date
        news = NewOffer.objects.all().order_by('priority', 'apply_date')
        return render(request, 'websites/news.html', {'news': news})
    except Exception, e:
        print "Error: ", e


def new_detail(request, id):
	try:
	    # get news detail by id
	    new = NewOffer.objects.get(pk=id)
	    return render(request, 'websites/new_detail.html', {'new': new})
	except NewOffer.ObjectDoesNotExist:
		print "Page not found !"
	except Exception, e:
		print "Error: ", e

def getCinemaTechnologyByName(request, name):
    try:
        allTechnology = CenimaTechnology.objects.all()
        technology = allTechnology.get(name=name)
        return render(request, 'websites/cinema_technology.html', {'technology': technology, 'allTechnology': allTechnology})
    except Exception, e:
    	print "Error: ", e

def home(request):
	try:
	    # banner on home page
	    result = {}
	    banners = Banner.objects.filter(is_show=True).order_by('position')
	    banner_position = {}
	    for item in banners:
	        banner_position[item.position] = item
	    result["banners"] = banner_position

	    # phim dang chieu
	    movie_showing = Movie.objects.filter(
	        release_date__lte=datetime.now()).order_by('priority', 'release_date')
	    # phim sap chieu
	    movie_soon = Movie.objects.filter(
	        release_date__gte=datetime.now()).order_by('priority', 'release_date')
	    # slide banner home page
	    data_slide = SlideShow.objects.all()
	    return render(request, 'websites/home.html', {'data_slide': data_slide, 'movie_soon': movie_soon, 'movie_showing': movie_showing, 'result': result})
	
	except Exception, e:
		print "Error: ", e