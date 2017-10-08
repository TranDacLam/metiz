# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import *
from django.db.models import Avg, Sum, Count
from django.http import HttpResponse, JsonResponse

data_schedule= [{
    'date':'2017-10-27',
    'film':[
        {'name': 'Yeu Di Dung So',
        'schedule': [
        {'from': '8:35', 'to': '10:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '21:35', 'to': '0:35', 'room': 119,'name_room': 'Scm01'},
        ] },
        {'name': 'The gioi nay la cua bo may',
        'schedule': [
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        ] },
        {'name': 'Chu he IT',
        'schedule': [
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        ]}
    ]},
    {
    'date':'2017-10-28',
    'film':[
        {'name': 'Yeu Di Dung So',
        'schedule': [
        {'from': '8:35', 'to': '10:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        
        ] },
        {'name': 'The gioi nay la cua bo may',
        'schedule': [
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        ] },
        {'name': 'Chu he IT',
        'schedule': [
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        ]}
    ]},
    {
    'date':'2017-10-29',
    'film':[
        {'name': 'Yeu Di Dung So',
        'schedule': [
        {'from': '8:35', 'to': '10:35', 'room': 119,'name_room': 'Scm01'},
        
        ] },
        {'name': 'The gioi nay la cua bo may',
        'schedule': [
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '21:35', 'to': '0:35', 'room': 119,'name_room': 'Scm01'},
        ] },
        {'name': 'Chu he IT',
        'schedule': [
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        {'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
        ]}
    ]},
    ]
data_celendar = {'last' : range(15,27),'present':range(27,30), 'future': range(1,15) }
def custom_404(request):
    return render(request, 'websites/errors/404.html', {}, status=404)


def custom_500(request):
    return render(request, 'websites/errors/500.html', {}, status=500)


def showing(request):
    try:
         # data for modal
        data_modal= data_schedule
        data_date=data_celendar
        # get data movie showing
        data_showing = Movie.objects.filter(
            release_date__lte=datetime.now(), is_draft=False).order_by('priority', 'release_date')
        return render(request, 'websites/showing.html', {'data_modal': data_modal, 'data_date':data_date,'data_showing': data_showing})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def coming_soon(request):
    try:
         # data for modal
        data_modal= data_schedule
        data_date=data_celendar
        # get data moving comingsoon
        data = Movie.objects.filter(release_date__gte=datetime.now(), is_draft=False).order_by(
            'priority', 'release_date')
        return render(request, 'websites/coming_soon.html', {'data_modal': data_modal, 'data_date':data_date,'data': data})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def film_detail(request, id):
    try:
         # data for modal
        data_modal= data_schedule
        data_date=data_celendar
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
        return render(request, 'websites/film_detail.html', {'data_modal': data_modal, 'data_date':data_date, 'total_percent': total_percent, 'count': count, 'rating__sum': rating__sum, 'film_detail': film_detail, 'comments': comments, 'rating__avg': rating__avg})
    except Movie.DoesNotExist, e:
        print "Error Movie : %s" % e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def news(request):
    try:
         # data for modal
        data_modal= data_schedule
        data_date=data_celendar
        # get news order by priority and apply_date
        news = NewOffer.objects.all().order_by('priority', 'apply_date')
        return render(request, 'websites/news.html', {'data_modal': data_modal, 'data_date':data_date ,'news': news})
    except Exception, e:
        print "Error: %s" % e
        return HttpResponse(status=500)


def new_detail(request, id):
    try:
         # data for modal
        data_modal= data_schedule
        data_date=data_celendar
        # get news detail by id
        new = NewOffer.objects.get(pk=id)
        return render(request, 'websites/new_detail.html', {'data_modal': data_modal, 'data_date':data_date, 'new': new})
    except NewOffer.DoesNotExist, e:
        print "Error new_detail : %s" % e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def technology_detail(request, name):
    try:
         # data for modal
        data_modal= data_schedule
        data_date=data_celendar
        # get technology detail by name
        allTechnology = CenimaTechnology.objects.all()
        technology = allTechnology.get(name=name)
        return render(request, 'websites/cinema_technology.html', {'data_modal': data_modal, 'data_date':data_date,  'technology': technology, 'allTechnology': allTechnology})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def home(request):
    try:
        # data for modal
        data_modal= data_schedule
        data_date=data_celendar
        # banner on home page
        result = {}
        banners = Banner.objects.filter(is_show=True).order_by('position')

        # check list banners and get banner position 1 and 2
        position_1, position_2 = None, None
        if banners:
            position_1 = banners.filter(position=1)
            position_2 = banners.filter(position=2)

        # phim dang chieu
        movie_showing = Movie.objects.filter(
            release_date__lte=datetime.now(), is_draft=False).order_by('priority', 'release_date')
        # phim sap chieu
        movie_soon = Movie.objects.filter(
            release_date__gte=datetime.now(), is_draft=False).order_by('priority', 'release_date')
        # slide banner home page
        data_slide = SlideShow.objects.filter(is_draft=False)
        print(data_date)
        return render(request, 'websites/home.html', { 'data_modal': data_modal, 'data_date':data_date,  'position_1': position_1, 'position_2': position_2, 'data_slide': data_slide, 'movie_soon': movie_soon, 'movie_showing': movie_showing})
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
