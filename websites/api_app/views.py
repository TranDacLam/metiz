from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView
from core.models import *
from core.custom_models import User
from api_app import serializers
from rest_framework.permissions import AllowAny
from registration import forms as forms_registration
from api import actions
from booking import api
from core.metiz_cipher import MetizAESCipher
import json
from booking.models import BookingInfomation
from rest_framework import status
from django.db.models import Q
from datetime import *

# Create your views here.


# Author: Lam
@api_view(['POST'])
@permission_classes((AllowAny, ))
def register(request):
    """
        - Use forms_registration from registration form
        - Return serialzer data
    """
    register_form = forms_registration.MetizSignupForm(
        request.data, request=request)

    if register_form.is_valid():
        register_form.save()
        return Response({"message": _('Register Account Successfully. Please Check Your Email and Active Account.')})

    return Response({'errors': register_form.errors}, status=400)


# Author: Lam
@permission_classes((AllowAny, ))
class BlogViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Blog.objects.filter(is_draft=False).order_by('-created', '-id')
    serializer_class = serializers.BlogSerializer


# Author: Lam
@permission_classes((AllowAny, ))
class FaqViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = FAQ_Category.objects.all()
    serializer_class = serializers.FaqCategorySerializer


# Author: Lam
class TransactionHistoryList(ListAPIView):

    def get(self, request, format=None):
        try:
            user_id = request.user.id
            lst_item = actions.get_booking_info_data(user_id, None, None, {'done'})
            return Response(lst_item['results'])

        except Exception, e:
            print 'TransactionHistoryList ', e
            error = {"code": 500, "message": _(
                "Internal Server Error"), "fields": ""}
            return Response(error, status=500)


# Author: Lam
class ProfileDetail(RetrieveUpdateAPIView):

    def get_card_member(self, user):
        # Get link card by user
        linkcard = LinkCard.objects.filter(user=user)
        # if user in link then get first linked
        card_member = linkcard.first().card_member if linkcard else ''
        return card_member

    def get(self, request, format=None):
        try:
            user = request.user
            card_member = self.get_card_member(user)
            serializer_user = serializers.ProfileSerializer(user, many=False)
            return Response({"user": serializer_user.data, "card_member": card_member})

        except Exception, e:
            print 'ProfileDetail ', e
            error = {"code": 500, "message": _(
                "Internal Server Error"), "fields": ""}
            return Response(error, status=500)

    def put(self, request, format=None):
        try:
            user = request.user
            profile_form = forms_registration.UpdateUserForm(
                request.data, user=user)
            if profile_form.is_valid():
                profile_data = profile_form.save()
                serializer = serializers.ProfileSerializer(
                    profile_data, many=False)
                return Response(serializer.data)
            return Response({"code": 400, "message": profile_form.errors, "fields": ""}, status=400)

        except Exception, e:
            print 'ProfileDetail PUT', e
            error = {"code": 500, "message": _(
                "Internal Server Error"), "fields": ""}
            return Response(error, status=500)


"""
    Function get_movie_seat
    Author: HoangNguyen
    Duplication: get_seats
"""


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_movie_seat(request):
    try:
        id_server = request.query_params.get('id_server', 1)
        id_showtime = request.query_params.get('id_showtime', None)

        if id_showtime:
            result = api.call_api_seats(id_showtime, id_server)
            return Response(result)
        error = {"code": 400, "message": _("Field id_showtime is required."),
                 "fields": "id_showtime"}
        return Response(error, status=400)
    except Exception, e:
        print "Error get_movie_seat : %s" % e
        return Response({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)

"""
    Function check_movie_seat
    Author: HoangNguyen
    Duplication: check_seats

"""


@api_view(['POST'])
@permission_classes((AllowAny, ))
def check_movie_seat(request):
    try:
        id_server = request.data.get('id_server', 1)
        id_showtime = request.data.get('id_showtime', None)
        seats_choice = request.data.get('seats_choice', None)

        if not seats_choice or not id_showtime:
            error = {"code": 400, "message": _("Fields id_showtime, seats_choice is required."),
                     "fields": "id_showtime, seats_choice"}
            return Response(error, status=400)
        data_seats = api.call_api_seats(id_showtime, id_server)

        if data_seats and data_seats["List"]:
            # step 1.Check seat is selected
            seat_has_selected = []
            total_money = 0
            for item in seats_choice:
                chair_is_choice = [str(s["NAME"]) for s in data_seats["List"] if s[
                    "ID"] == item["ID"] and s["STATUS"] == "True"]
                total_money += sum(int(s["PRICE"]) for s in data_seats["List"] if s[
                    "ID"] == item["ID"])
                if chair_is_choice:
                    seat_has_selected.append(chair_is_choice[0])

            if seat_has_selected:
                return Response({"code": 400, "message": _("These chairs have been selected ") + str(seat_has_selected)}, status=400)

            # step 2.Lock seat
            full_name = request.data.get('full_name', None)
            phone = request.data.get('phone', None)
            email = request.data.get('email', None)

            if not full_name or not phone:
                error = {"code": 400, "message": _("Fields full_name, phone is required."),
                         "fields": "id_showtime, seats_choice"}
                return Response(error, status=400)
            # remove uni
            seats_choice_clean = json.dumps(seats_choice)
            url = "/postBooking"
            result = api.call_api_post_booking(
                full_name, phone, email, seats_choice_clean, id_server, None, url)

            if not result["BARCODE"] or str(result["BARCODE"]) == '0' or total_money <= 0:
                print "***** Get Barcode Fail : ", result
                return Response({"code": 400, "message": _("Cannot Booking Seats. Please Contact Administrator.")}, status=400)

            # step 3.Save bookingInfomation
            seats = str([int(item['ID']) for item in seats_choice]).strip('[]')
            bookingSerializer = serializers.BookingInfomationSerializer(data=request.data, context={
                                                                        'amount': total_money, 'seats': seats, 'barcode': result["BARCODE"]})
            if bookingSerializer.is_valid():
                bookingSerializer.save()
                return Response(bookingSerializer.data)
            return Response(bookingSerializer.errors, status=400)
        return Response({"code": 400, "message": _("Not found showtime for id_showtime")}, status=400)

    except Exception, e:
        print "Error check_movie_seat : %s" % e
        return Response({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)

"""
    Function verify_card_member
    Author: HoangNguyen
    Duplication: verify_card_member from api/views.py
    Decription: verify card_member and decrpyt working_id

"""


@api_view(['POST'])
@permission_classes((AllowAny, ))
def verify_card_member(request):
    try:
        card_member = request.data.get('card_member', None)
        working_id = request.data.get('working_id', None)

        if not card_member or not working_id:
            return Response({"code": 400, "message": _(
                "Card member and Working_id are required."), "fields": "card_member, working_id"}, status=400)
        # Step 1: check card_member
        responses = actions.verify_card_member_pos(card_member)

        if responses["code"] != 200:
            return Response(responses, status=responses["code"])

        if not responses['data']['result_verify_card']:
            return Response({"code": 400, "message": _("Card member not found."), "fields": ""}, status=400)

        # Step 2: decrypt working_id
        cipher = MetizAESCipher()

        try:
            working_decrypt = cipher.decrypt(working_id)
        except Exception, e:
            print "Exception working_decrypt", e
            return Response({"code": 400, "message": _("Working_id is incorrect"), "fields": "Working_id"}, status=400)

        # Step 3: add card_member to booking
        booking = BookingInfomation.objects.get(working_id=working_decrypt)
        booking.card_member = card_member
        booking.save()
        return Response({"code": 200, "message": _("Success.")}, status=200)

    except BookingInfomation.DoesNotExist, e:
        print "Error verify_card_member : %s" % e
        return Response({"code": 400, "message": _("Not found BookingInfomation.")}, status=400)
    except Exception, e:
        print "Error verify_card_member : %s" % e
        return Response({"code": 500, "message": _("Internal Server Error. Please contact administrator.")}, status=500)



"""
 Decription: get showing movie
 Author: HoangNguyen
"""
class ShowingList(ListAPIView):
    serializer_class = serializers.MovieSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        movie_showings = Movie.objects.filter(Q(end_date__isnull=True) | Q(end_date__gte=datetime.now()), release_date__lte=datetime.now(), is_draft=False).extra(
            select={'priority_null': 'priority is null'})
        list_data_showing = movie_showings.extra(
            order_by=['priority_null', 'priority', '-release_date', 'name'])
        return list_data_showing

"""
Decription: get comming movie
Author: HoangNguyen
"""
class CommingList(ListAPIView):
    serializer_class = serializers.MovieSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        movie_comming = Movie.objects.filter(
            release_date__gt=datetime.now(), is_draft=False).extra(select={'priority_null': 'priority is null'})
        list_data_coming_soon = movie_comming.extra(
            order_by=['priority_null', 'release_date', 'name'])
        return list_data_coming_soon

"""
Decription: get detail movie
Author: HoangNguyen
"""
class DetailMovie(RetrieveAPIView):
    serializer_class = serializers.MovieSerializer
    permission_classes = (AllowAny,)
    queryset = Movie
