# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import *
from django.db.models import Avg, Sum, Count
from django.http import HttpResponse


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
        return HttpResponse(status=500)

def coming_soon(request):
    try:
        # get data moving comingsoon
        data = Movie.objects.filter(release_date__gte=datetime.now()).order_by(
            'priority', 'release_date')
        return render(request, 'websites/coming_soon.html', {'data': data})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


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

        total_percent = []
        for i in range(1, 6):
            # lay tong so sao cung loai (1 sao, 2 sao,...5 sao) trong danh gia
            count = comments.filter(rating=i).aggregate(
                Sum('rating')).get('rating__sum')
            # dua tong so sao tung loai vao mang
            total_percent.append(count)
        return render(request, 'websites/film_detail.html', {'total_percent': total_percent, 'count': count, 'rating__sum': rating__sum, 'film_detail': film_detail, 'comments': comments, 'rating__avg': rating__avg})
    except Movie.DoesNotExist, e:
        print "Error Movie : %s"%e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)

def news(request):
    try:
        # get news order by priority and apply_date
        news = NewOffer.objects.all().order_by('priority', 'apply_date')
        return render(request, 'websites/news.html', {'news': news})
    except Exception, e:
        print "Error: %s"%e
        return HttpResponse(status=500)

def new_detail(request, id):
    try:
        # get news detail by id
        new = NewOffer.objects.get(pk=id)
        return render(request, 'websites/new_detail.html', {'new': new})
    except NewOffer.DoesNotExist, e:
        print "Error new_detail : %s"%e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)

def getCinemaTechnologyByName(request, name):
    try:
        allTechnology = CenimaTechnology.objects.all()
        technology = allTechnology.get(name=name)
        return render(request, 'websites/cinema_technology.html', {'technology': technology, 'allTechnology': allTechnology})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)

def home(request):
    try:
        # banner on home page
        result = {}
        banners = Banner.objects.filter(is_show=True).order_by('position')
        
        position_1 = banners[0].position
        image_1 = banners[0].image
        sub_url_1 = banners[0].sub_url

        position_2 = banners[1].position
        image_2 = banners[1].image
        sub_url_2 = banners[1].sub_url

        # phim dang chieu
        movie_showing = Movie.objects.filter(
            release_date__lte=datetime.now()).order_by('priority', 'release_date')
        # phim sap chieu
        movie_soon = Movie.objects.filter(
            release_date__gte=datetime.now()).order_by('priority', 'release_date')
        # slide banner home page
        data_slide = SlideShow.objects.all()
        return render(request, 'websites/home.html', {'image_1':image_1,'image_2':image_2,'sub_url_1':sub_url_1,'sub_url_2':sub_url_2,'position_1':position_1,'position_2':position_2,'banners':banners,'data_slide': data_slide, 'movie_soon': movie_soon, 'movie_showing': movie_showing})
    except Movie.DoesNotExist, e:
        print "Error Movie : %s"%e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)

def get_post(request):
    try:
        if 'id' in request.GET:
            item = Post.objects.get(pk=request.GET['id'])
        elif 'key_query' in request.GET:
            item = Post.objects.get(key_query=request.GET['key_query'])
        return render(request, 'websites/cms.html', {'item': item})
    except Post.DoesNotExist, e:
        print "Error get_post : id or key_query does not exist"
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)
