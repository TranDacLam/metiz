from rest_framework import serializers
from core.custom_models import User
from core.models import *


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'