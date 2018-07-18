from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from core.models import *
from core.custom_models import User
from api_app import serializers
from rest_framework.permissions import AllowAny
from registration import forms
# Create your views here.


@permission_classes((AllowAny, ))
class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
        - Only use create
        - Use forms from registration form
        - Return serialzer data
    """
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer

    def create(self, request):
        register_form = forms.MetizSignupForm(request.data, request=request)

        if register_form.is_valid():
            register_data = register_form.save()
            serializer = serializers.RegisterSerializer(register_data)
            return Response(serializer.data)

        return Response({'errors': register_form.errors}, status=400)


@permission_classes((AllowAny, ))
class BlogViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get_queryset(self):
        return self.queryset.filter(is_draft=False).order_by('-created', '-id')


@permission_classes((AllowAny, ))
class FaqViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = FAQ_Category.objects.all()
    serializer_class = serializers.FaqCategorySerializer