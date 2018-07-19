from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from core.models import *
from core.custom_models import User
from api_app import serializers
from rest_framework.permissions import AllowAny
from registration import forms as forms_registration
from api import actions
# Create your views here.


# Author: Lam
@api_view(['POST'])
@permission_classes((AllowAny, ))
def register(request):
    """
        - Use forms_registration from registration form
        - Return serialzer data
    """
    register_form = forms_registration.MetizSignupForm(request.data, request=request)

    if register_form.is_valid():
        register_data = register_form.save()
        serializer = serializers.RegisterSerializer(register_data)
        return Response(serializer.data)

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
            profile_form = forms_registration.UpdateUserForm(request.data, user=user)
            if profile_form.is_valid():
                profile_data = profile_form.save()
                serializer = serializers.ProfileSerializer(profile_data, many=False)
                return Response(serializer.data)
            return Response({"code": 400, "message": profile_form.errors, "fields": ""}, status=400)

        except Exception, e:
            print 'ProfileDetail PUT', e
            error = {"code": 500, "message": _(
                "Internal Server Error"), "fields": ""}
            return Response(error, status=500)