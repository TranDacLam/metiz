# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from models import *
from datetime import *
from django.db.models import Avg, Sum, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from itertools import chain
from django.core.urlresolvers import reverse
import itertools
from core.forms import ContactForm
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib.sites.models import Site
from registration import metiz_email
from random import randint
from django.contrib.auth.decorators import login_required

# NOTES : View SQL Query using : print connection.queries


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
            # Ajax reuqest with page, render page and return to client
            return render(request, 'websites/load_movie_render.html', {'list_data_film': movie_page.object_list})

        return render(request, 'websites/list_film.html', {'list_data_film': movie_page.object_list, 'total_page': paginator.num_pages,
                                                           'title': "Phim Đang Chiếu"})
    except Exception, e:
        print "Error action showing: ", e
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
            return render(request, 'websites/load_movie_render.html', {'list_data_film': movie_page.object_list})

        return render(request, 'websites/list_film.html', {'list_data_film': movie_page.object_list, 'total_page': paginator.num_pages,
                                                           'title': "Phim Sắp Chiếu"})
    except Exception, e:
        print "Error action : ", e
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
        # Calculated percent of rating
        percent = {'5': 0, '4': 0, '3': 0, '2': 0, '1': 0}

        for r in total_detail:
            percent[str(r['rating'])] = r["total"] * 100 / total_count

        return render(request, 'websites/film_detail.html',
                      {'total_count': total_count, 'rating_percent': percent, 'rating__avg': rating__avg,
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

        list_news_future = news.filter(apply_date__gt=datetime.now()).order_by(
            'apply_date', 'created')

        # get news present
        list_news_present = news.filter(apply_date__lte=datetime.now()).order_by(
            '-apply_date', '-created', 'name')

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
            print news_json
            for item in news_page.object_list:
                news_json.append({"id": item.id, "image": str(
                    item.image), "apply_date": item.apply_date, "name": item.name, "end_date": item.end_date})
            # convert object models to json
            # Ajax reuqest with page, db get data other with limit and offset

            return JsonResponse({"data": news_json}, safe=False)

        return render(request, 'websites/news.html', {'list_news': news_page.object_list, 'total_page': paginator_news.num_pages})
    except Exception, e:
        print "Error: %s" % e
        return HttpResponse(status=500)


def new_detail(request, id):
    try:
        # get news detail by id
        new = NewOffer.objects.get(pk=id)
        return render(request, 'websites/new_detail.html', {'new': new})
    except NewOffer.DoesNotExist, e:
        print "Error action new_detail : %s" % e
        return HttpResponse(status=404)
    except Exception, e:
        print "Error action new_detail : ", e
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
        print "Error action get_technology : ", e
        return JsonResponse(status=500)


def technology_detail(request, name):
    try:
        # get all technology for menu
        allTechnology = CenimaTechnology.objects.all()
        # get technology detail by name
        technology = allTechnology.get(name=name)
        return render(request, 'websites/cinema_technology.html', {'technology': technology, 'allTechnology': allTechnology})
    except Exception, e:
        print "Error action technology_detail : ", e
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
            order_by=['priority_null', 'priority', '-release_date', 'name'])

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
            order_by=['priority_null', 'priority', 'release_date', 'name'])

        # get news order by priority and apply_date
        news = NewOffer.objects.all().order_by('priority').extra(
            select={'priority_null': 'priority is null'})

        top_news = news.extra(
            order_by=['priority_null', 'priority', '-created'])[:5]

        # slide banner home page
        data_slide = SlideShow.objects.filter(is_draft=False)

        # get post item new and offer
        try:
            new_offer = Post.objects.get(
                key_query='kq_new_offer', is_draft=False)

        except Post.DoesNotExist, e:
            print "Error Post : %s" % e
            new_offer = None
        return render(request, 'websites/home.html', {'top_news': top_news, 'list_showing': list_showing,
                                                      'list_coming_soon': list_coming_soon,
                                                      'position_1': position_1[0] if position_1 else None,
                                                      'position_2': position_2[0] if position_2 else None,
                                                      'data_slide': data_slide, 'new_offer': new_offer})

    except Exception, e:
        print "Error action home : ", e
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
        print "Error action get_post : ", e
        return HttpResponse(status=500)


def contacts(request):
    """
        Send Contact to metiz administrator
        step 1 : validate data
        step 2 : data is valid then save to database end send mail to admin
    """
    try:
        contact_form = ContactForm()
        if request.method == "POST":
            contact_form = ContactForm(request.POST)
            # check form valid
            if contact_form.is_valid():
                contact_form.save(is_secure=request.is_secure())
                messages.success(request, _('Send Contact Successfully.'))

        return render(request, 'websites/contacts.html', {"forms": contact_form})
    except Exception as e:
        print "Error action contacts : ", e
        return HttpResponse(status=500)


def blog_film(request):
    try:
        if request.method == "POST":
            page_items = request.POST.get('page_items', 9)
            page_number = request.POST.get('page', 1)
            order_colunm = request.POST.get('order_column', '-created')

            # Get all blogs film by Id order by created
            blogs = Blog.objects.filter(
                is_draft=False).order_by(order_colunm, '-id')

            # Pagination QuerySet With Defalt Page is 9 Items
            paginator = Paginator(blogs, page_items)

            try:
                blog_page = paginator.page(int(page_number))
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                return JsonResponse({"message": _("Page Number Not Type Integer.")}, status=400)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of
                # results.
                return JsonResponse({"message": _("Page Number Not Found.")}, status=400)

                # convert object models to json
                # Ajax reuqest with page, render page and return to client
            return render(request, 'websites/ajax/list_blog_film.html', {'list_blogs': blog_page.object_list, 'total_page': paginator.num_pages})

        return render(request, 'websites/blog_film.html')

    except Exception as e:
        print "Error action blog_film : ", e
        return HttpResponse(status=500)


def blog_film_detail(request, id):
    try:
        # init view counter is 0
        view_counter = 0
        related_blogs = []

        # get blog detail by id
        blog = Blog.objects.get(pk=id)

        if blog:
            # get hit count of blog objects
            view_counter = blog.hit_count.hits

            # count a hit and get the response
            hit_count_response = HitCountMixin.hit_count(
                request, blog.hit_count)

            # if response.hit_counted is True then hit count success
            if hit_count_response.hit_counted:
                view_counter = view_counter + 1

            # get blog detail by id
            related_blogs = Blog.objects.filter(
                ~Q(id=blog.id), is_draft=False).order_by('-created')[:4]

        return render(request, 'websites/blog_film_detail.html',
                      {'blog': blog, 'related_blogs': related_blogs, 'view_counter': view_counter})
    except Exception as e:
        print "Error action blog_film_detail : ", e
        return HttpResponse(status=500)

""" 10000 VOUCHER FREE """


def voucher(request):
    try:
        if request.method == "POST":
            # Set deadline to get voucher 17:00 14/02/2017
            deadline =  datetime(2018, 2, 14, 17, 00, 00, 00000)
            # Check time get voucher valid
            if datetime.now() > deadline:
                return JsonResponse({'message': _('voucher time out')})

            if not request.user.is_anonymous():
                user = request.user
                # Get voucher by current user login
                voucher_by_user = Voucher.objects.filter(user=user)

                # Check user have got voucher
                if voucher_by_user.exists():
                    return JsonResponse({'code': voucher_by_user.get().voucher_code})

                # Get list voucher free
                voucher_list = Voucher.objects.filter(
                    ~Q(status__in=('linked', 'received')))
                # Get size of voucher list
                count = voucher_list.count()

                # Check out of voucher code
                if count == 0:
                    return JsonResponse({'message': _('Out of voucher code')})

                # Get voucher code by random
                voucher = voucher_list[randint(0, count - 1)]

                if voucher:
                    voucher.user = user
                    voucher.status = 'linked'
                    voucher.save()

                    send_mail_voucher(
                        request.is_secure(), user.email, user.full_name, voucher.voucher_code)
                    return JsonResponse({'code': voucher.voucher_code})

            else:
                return JsonResponse({'message': _('Please login to received voucher')})

        return render(request, 'websites/voucher.html')
    except Exception as e:
        print "Error action voucher : ", e
        return HttpResponse(status=500)

"""Send mail to user"""


def send_mail_voucher(is_secure, email, full_name, barcode):
    try:
        message_html = "websites/email/voucher_email.html"
        subject = _("[Metiz] Voucher Code !")

        protocol = 'http'
        if is_secure:
            protocol = 'https'
        logo_url = '/static/assets/websites/images/logo_bottom.png'
        data_binding = {
            "protocol": protocol,
            'full_name': full_name,
            'URL_LOGO': logo_url,
            'barcode': barcode,
            'site': str(Site.objects.get_current()),
            'HOT_LINE': settings.HOT_LINE
        }
        # Send email booking success
        metiz_email.send_mail(subject, None, message_html, settings.DEFAULT_FROM_EMAIL, [
                              email], data_binding)
    except Exception, e:
        print "Error send_mail_booking : ", e
