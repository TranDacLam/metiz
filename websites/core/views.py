# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from models import *
from datetime import *
from django.db.models import Avg, Sum, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from itertools import chain
from booking.forms import BookingForm
from django.core.urlresolvers import reverse
import itertools

# NOTES : View SQL Query using : print connection.queries


def custom_404(request):
    return render(request, 'websites/errors/404.html', {}, status=404)


def custom_500(request):
    return render(request, 'websites/errors/500.html', {}, status=500)


def showing(request):
    try:
        # get data movie showing
        """ 
            Movie Showing Follow Condition:
            - get movie with release date less than equal current day
            - order priority first
            - order by field release_date descending
            - order by name
            *Note: in alogilm query movie add extra field priority_null and append priority is null to end list
        """
        page_items = request.GET.get('page_items', 12)
        page_number = request.GET.get('page', 1)

        movie_showings = Movie.objects.filter(
            release_date__lte=datetime.now(), end_date__gte=datetime.now(), is_draft=False).order_by('priority').extra(
            select={'priority_null': 'priority is null'})

        list_data_showing = movie_showings.extra(
            order_by=['priority_null', '-release_date', 'name'])

        # Pagination QuerySet With Defalt Page is 12 Items

        paginator = Paginator(list_data_showing, page_items)
        try:
            movie_page = paginator.page(int(page_number))
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            return JsonResponse({"message": _("Page Number Not Type Integer.")}, status=400)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            return JsonResponse({"message": _("Page Number Not Found.")}, status=400)

        if request.is_ajax():
            # convert object models to json
            # Ajax reuqest with page, db get data other with limit and offset
            return JsonResponse({"data": list(movie_page.object_list.values('id', 'name', 'poster', 'time_running', 'release_date', "genre__name", "rated__name")),
                                 "total_page": paginator.num_pages}, safe=False)

        return render(request, 'websites/showing.html', {'list_data_showing': movie_page.object_list})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def coming_soon(request):
    try:
        # get data moving comingsoon
        """ 
            Movie Comming Soon Follow Condition:
            - get movie with release date greater than current day
            - order priority first
            - order by field release_date descending
            - order by name
            *Note: in alogilm query movie add extra field priority_null and append priority is null to end list
        """
        page_items = request.GET.get('page_items', 12)
        page_number = request.GET.get('page', 1)

        movie_comming = Movie.objects.filter(
            release_date__gt=datetime.now(), is_draft=False).extra(select={'priority_null': 'priority is null'})

        list_data_coming_soon = movie_comming.extra(
            order_by=['priority_null', 'release_date', 'name'])

        # Pagination QuerySet With Defalt Page is 12 Items
        paginator = Paginator(list_data_coming_soon, page_items)
        try:
            movie_page = paginator.page(int(page_number))
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            return JsonResponse({"message": _("Page Number Not Type Integer.")}, status=400)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            return JsonResponse({"message": _("Page Number Not Found.")}, status=400)

        if request.is_ajax():
            # convert object models to json
            # Ajax reuqest with page, db get data other with limit and offset
            return JsonResponse({"data": list(movie_page.object_list.values('id', 'name', 'poster', 'time_running', 'release_date', "genre__name", "rated__name")),
                                 "total_page": paginator.num_pages}, safe=False)

        return render(request, 'websites/coming_soon.html', {'list_data_coming_soon': movie_page.object_list})
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
        # Count total user rating for film
        total_count = comments.aggregate(Count('rating')).get('rating__count')
        total_detail = comments.values(
            'rating').annotate(total=Count('rating')).order_by('-rating')

        return render(request, 'websites/film_detail.html',
                      {'total_count': total_count, 'total_detail': total_detail, 'rating__avg': rating__avg,
                       'film_detail': film_detail, 'comments': comments})

    except Movie.DoesNotExist, e:
        print "Error Movie : %s" % e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def news(request):
    try:
        """ 
            New and Offer for Furute then order by priority and apply_date ascending
            New and Offer for Present then order by priority and apply_date descending
            - If same date then order modified date
            *Note: in alogilm query movie add extra field priority_null and append priority is null to end list
        """

        page_items = request.GET.get('page_items', 12)
        page_number = request.GET.get('page', 1)

        # get news all
        news = NewOffer.objects.all()

        news_future = news.filter(apply_date__gt=datetime.now()).order_by(
            'priority').extra(select={'priority_null': 'priority is null'})

        list_news_future = news_future.extra(
            order_by=['priority_null', 'apply_date', 'modified'])

        # get news present
        news_present = news.filter(apply_date__lte=datetime.now()).order_by(
            'priority').extra(select={'priority_null': 'priority is null'})

        list_news_present = news_present.extra(
            order_by=['priority_null', '-apply_date', 'modified'])

        # merge 3 list by order future, present and past
        list_news = list(chain(list_news_future, list_news_present))

        # Pagination QuerySet With Defalt Page is 12 Items
        paginator_news = Paginator(list_news, page_items)
        try:
            news_page = paginator_news.page(int(page_number))
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            return JsonResponse({"message": _("Page Number Not Type Integer.")}, status=400)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            return JsonResponse({"message": _("Page Number Not Found.")}, status=400)

        if request.is_ajax():
            news_json = []
            for item in news_page.object_list:
                news_json.append({"id": item.id, "image": str(
                    item.image), "apply_date": item.apply_date})
            # convert object models to json
            # Ajax reuqest with page, db get data other with limit and offset
            
            return JsonResponse({"data": news_json, "total_page": paginator_news.num_pages}, safe=False)

        return render(request, 'websites/news.html', {'list_news': news_page.object_list, "total_item": len(news_page.object_list)})
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


def get_technology(request):
    try:
        if 'name' in request.GET:
            req_name = request.GET['name']
            # get technology detail by name
            try:
                technology = CenimaTechnology.objects.get(name=req_name)
                content = technology.content
                name = technology.name
                data = {
                    'name': name,
                    'content': content
                }
                return JsonResponse(data)
            except CenimaTechnology.DoesNotExist, e:
                print "Error get_technology ", e
                return JsonResponse({"message": "Technology Does Not Exist"}, status=400)

    except Exception, e:
        print "Error: ", e
        return JsonResponse(status=500)


def technology_detail(request, name):
    try:
        # get all technology for menu
        allTechnology = CenimaTechnology.objects.all()
        # get technology detail by name
        technology = allTechnology.get(name=name)
        return render(request, 'websites/cinema_technology.html', {'technology': technology, 'allTechnology': allTechnology})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)


def home(request):
    try:
        # banner on home page
        result = {}
        banners = Banner.objects.filter(
            is_show=True).order_by('position', 'modified')

        # check list banners and get banner position 1 and 2
        position_1, position_2 = None, None
        if banners:
            position_1 = banners.filter(position=1)
            position_2 = banners.filter(position=2)

        """ 
            Movie Showing Follow Condition:
            - get movie with release date less than equal current day
            - order priority first
            - order by field release_date descending
            - order by name
            *Note: in alogilm query movie add extra field priority_null and append priority is null to end list
        """
        movie_showings = Movie.objects.filter(
            release_date__lte=datetime.now(), end_date__gte=datetime.now(), is_draft=False).order_by('priority').extra(
            select={'priority_null': 'priority is null'})

        list_showing = movie_showings.extra(
            order_by=['priority_null', '-release_date', 'name'])

        """ 
            Comming Soon Follow Condition:
            - get movie with release date greater than current day
            - order priority first
            - order by field release_date descending
            - order by name
            *Note: in alogilm query movie add extra field priority_null and append priority is null to end list
        """
        movie_soons = Movie.objects.filter(
            release_date__gt=datetime.now(), is_draft=False).order_by('priority').extra(
            select={'priority_null': 'priority is null'})

        list_coming_soon = movie_soons.extra(
            order_by=['priority_null', 'release_date', 'name'])

        # get news order by priority and apply_date
        news = NewOffer.objects.all().order_by('priority').extra(
            select={'priority_null': 'priority is null'})

        top_news = news.extra(order_by=['priority_null', 'apply_date'])[:5]

        # slide banner home page
        data_slide = SlideShow.objects.filter(is_draft=False)

        #get post item new and offer
        new_offer = Post.objects.get(key_query='kq_new_offer', is_draft=False)

        return render(request, 'websites/home.html', {'top_news': top_news, 'list_showing': list_showing,
                                                      'list_coming_soon': list_coming_soon,
                                                      'position_1': position_1[0] if position_1 else None,
                                                      'position_2': position_2[0] if position_2 else None,
                                                      'data_slide': data_slide, 'new_offer': new_offer})
    except Post.DoesNotExist, e:
        print "Error Post : %s" % e
        return HttpResponse(status=404)
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


def get_booking(request):
    try:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                full_name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                id_showtime = form.cleaned_data['id_showtime']
                email = form.cleaned_data['email']
                request.session['full_name'] = full_name
                request.session['phone'] = phone
                request.session['email'] = email if email else None
                id_sever = 1
                print('*******booking******')
                return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_sever": id_sever})          
        else:
            print('*******booking******')
            id_showtime = request.GET['id_showtime']
            id_sever = request.GET['id_sever']
            return render(request, 'websites/booking.html', {"id_showtime": id_showtime, "id_sever": id_sever})
    except Exception, e:
        print "Error: ", e
        return HttpResponse(status=500)
