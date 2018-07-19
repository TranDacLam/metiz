from rest_framework import serializers
from core.custom_models import User
from core.models import *


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = '__all__'


class FaqCategorySerializer(serializers.ModelSerializer):
    faq_category_rel = serializers.SerializerMethodField('get_faqs')

    class Meta:
        model = FAQ_Category
        fields = ('id', 'name', 'faq_category_rel')

    def get_faqs(self, instance):
        query_set = FAQ.objects.filter(category__id=instance.id).order_by('question')
        serializer = FaqSerializer(query_set, many=True, read_only=True)
        return serializer.data


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
