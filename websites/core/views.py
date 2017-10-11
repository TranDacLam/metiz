# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import *
from django.db.models import Avg, Sum, Count
from django.http import HttpResponse, JsonResponse
from itertools import chain

def custom_404(request):
    return render(request, 'websites/errors/404.html', {}, status=404)


def custom_500(request):
    return render(request, 'websites/errors/500.html', {}, status=500)


def showing(request):
    try:
        # get data movie showing
        data_showing = Movie.objects.filter(
            release_date__lte=datetime.now(), is_draft=False)

        # get movie by priority !=null
        data_showing_has = data_showing.order_by('priority', 'release_date', 'name').exclude(priority__isnull=True)
        # get movie by priority ==null
        data_showing_null = data_showing.order_by('release_date','name').exclude(priority__isnull=False)
        # merge 2 queryset film_showing
        list_data_showing = list(chain(data_showing_has, data_showing_null))
        return render(request, 'websites/showing.html', {'list_data_showing': list_data_showing})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def coming_soon(request):
    try:
        # get data moving comingsoon
        data_coming_soon = Movie.objects.filter(release_date__gt=datetime.now(), is_draft=False)

        # get movie by priority !=null
        data_coming_soon_has = data_coming_soon.order_by('priority', 'release_date', 'name').exclude(priority__isnull=True)
        # get movie by priority ==null
        data_coming_soon_null = data_coming_soon.order_by('release_date','name').exclude(priority__isnull=False)
        # merge 2 queryset film_showing
        list_data_coming_soon = list(chain(data_coming_soon_has, data_coming_soon_null))
        return render(request, 'websites/coming_soon.html', {'list_data_coming_soon': list_data_coming_soon})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def film_detail(request, id):
    try:
        # get film detail by id
        film_detail = Movie.objects.get(pk=id, is_draft=False)
        # filter comments of film detail by movie_id
        comments = Comment.objects.filter(movie=film_detail.id)
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
        print "Error Movie : %s" % e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def news(request):
    try:
        # get news order by priority and apply_date
        news = NewOffer.objects.all()
        # get news by priority !=null
        data_news_has = news.order_by('priority', 'apply_date').exclude(priority__isnull=True)
        # get news by priority=null
        data_news_null = news.order_by('apply_date').exclude(priority__isnull=False)
        # merge 2 queryset news
        list_news = list(chain(data_news_has, data_news_null))
        
        return render(request, 'websites/news.html', {'list_news': list_news})
    except Exception, e:
        print "Error: %s" % e
        return HttpResponse(status=500)


def new_detail(request, id):
    try:
        # get news detail by id
        new = NewOffer.objects.get(pk=id)
        return render(request, 'websites/new_detail.html', {'new': new})
    except NewOffer.DoesNotExist, e:
        print "Error new_detail : %s" % e
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
        banners = Banner.objects.filter(is_show=True).order_by('position', 'modified')

        # check list banners and get banner position 1 and 2
        position_1, position_2 = None, None
        if banners:
            position_1 = banners.filter(position=1)
            position_2 = banners.filter(position=2)

        # phim dang chieu
        movie_showing = Movie.objects.filter(
            release_date__lte=datetime.now(), is_draft=False)
        # get movie by priority !=null
        film_showing_has = movie_showing.order_by('priority', 'release_date', 'name').exclude(priority__isnull=True)
        # get movie by priority ==null
        film_showing_null = movie_showing.order_by('release_date','name').exclude(priority__isnull=False)
        # merge 2 queryset film_showing
        list_showing = list(chain(film_showing_has, film_showing_null))
        
        # phim sap chieu
        movie_soon = Movie.objects.filter(
            release_date__gt=datetime.now(), is_draft=False)
        # get movie by priority !=null
        film_coming_soon_has = movie_soon.order_by('priority', 'release_date', 'name').exclude(priority__isnull=True)
        # get movie by priority ==null
        film_coming_soon_null = movie_soon.order_by('release_date','name').exclude(priority__isnull=False)
        # merge 2 queryset film_coming_soon
        list_coming_soon = list(chain(film_coming_soon_has, film_coming_soon_null))

        # slide banner home page
        data_slide = SlideShow.objects.filter(is_draft=False)
        return render(request, 'websites/home.html', {'list_showing':list_showing,'list_coming_soon':list_coming_soon,'position_1': position_1[0] if position_1 else None, 'position_2': position_2[0] if position_2 else None, 'data_slide': data_slide})
    except Movie.DoesNotExist, e:
        print "Error Movie : %s" % e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def get_post(request):
    """ Get Post by id or key query """
    try:
        if 'id' in request.GET:
            item = Post.objects.get(pk=request.GET['id'], is_draft=False)
        elif 'key_query' in request.GET:
            item = Post.objects.get(key_query=request.GET[
                                    'key_query'], is_draft=False)

        # If request call ajax then return json
        if request.is_ajax():
            # convert object models to json
            result = {}
            if item:
                result['id'] = item.id
                result['name'] = item.name
                result['content'] = item.content
                result['key_query'] = item.key_query
            return JsonResponse(result)

        return render(request, 'websites/cms.html', {'item': item})
    except Post.DoesNotExist, e:
        print "Error get_post : id or key_query does not exist"
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)
