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
    new_favourite_rel = serializers.SerializerMethodField('get_favourite')

    class Meta:
        model = NewOffer
        fields = '__all__'

    def get_favourite(self, instance):
        user_id = self.context['request'].user.id
        query_set = Favourite_NewOffer.objects.filter(new__id=instance.id, user__id=user_id)
        favourite_id = query_set.first().id if query_set else ''
        return favourite_id


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


class FavouriteNewOfferSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    new = NewSerializer(many=False, read_only=True)

    class Meta:
        model = Favourite_NewOffer
        fields = '__all__'

    def to_internal_value(self, data):
        self.fields['new'] = serializers.PrimaryKeyRelatedField(queryset=NewOffer.objects.all())
        return super(FavouriteNewOfferSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        representation = super(FavouriteNewOfferSerializer, self).to_representation(instance)
        if self.context['request'].method == "GET":
            """New fields from Favourite NewOffer to New representation."""
            favourite_representation = representation.pop('new')
            for key in favourite_representation:
                representation[key] = favourite_representation[key]
            return representation

        return representation


class MovieTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieType
        exclude = ('created', 'modified')

class RatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rated
        exclude = ('created', 'modified')

class MovieSerializer(serializers.ModelSerializer):
    movie_type = MovieTypeSerializer(many = False)
    rated = RatedSerializer(many = False)
    movie_favourite_rel = serializers.SerializerMethodField('get_favourite')
    
    class Meta:
        model = Movie
        exclude = ('created', 'modified')

    def get_favourite(self, instance):
        user_id = self.context['request'].user.id
        query_set = Favourite_Movie.objects.filter(movie__id=instance.id, user__id=user_id)
        favourite_id = query_set.first().id if query_set else ''
        return favourite_id


class FavouriteMovieSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    movie = MovieSerializer(many=False, read_only=True)

    class Meta:
        model = Favourite_Movie
        fields = '__all__'

    def to_internal_value(self, data):
        self.fields['movie'] = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
        return super(FavouriteMovieSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        representation = super(FavouriteMovieSerializer, self).to_representation(instance)
        if self.context['request'].method == "GET":
            """Movie fields from Favourite Movie to Movie representation."""
            favourite_representation = representation.pop('movie')
            for key in favourite_representation:
                representation[key] = favourite_representation[key]
            return representation

        return representation