from rest_framework import serializers
from core.custom_models import User
from core.models import *
from booking.models import BookingInfomation
import datetime
import time
import uuid
from core.metiz_cipher import MetizAESCipher

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


class NewSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewOffer
        fields = '__all__'


class BookingInfomationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingInfomation
        exclude = ('created', 'modified')

    # set value before validate
    def to_internal_value(self, data):
        if 'amount' in self.context and 'seats' in self.context and 'barcode' in self.context:
            data['amount'] = self.context['amount']
            data['seats'] = self.context['seats']
            data['barcode'] = self.context['barcode']
            data['working_id'] = str(uuid.uuid1())
            data['order_status'] = "pendding"
            data['order_id'] = int(time.mktime(datetime.datetime.now().timetuple())*1e3 + datetime.datetime.now().microsecond/1e3)
            data['system_name'] = "metiz_app"
        return super(BookingInfomationSerializer, self).to_internal_value(data)
    
    # encrypt working_id to return Response
    def to_representation(self, instance):
        cipher = MetizAESCipher()
        instance.working_id = cipher.encrypt(str(instance.working_id))
        return super(BookingInfomationSerializer, self).to_representation(instance)


class FavouriteMovieSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favourite_Movie
        fields = '__all__'


class FavouriteNewOfferSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favourite_NewOffer
        fields = '__all__'