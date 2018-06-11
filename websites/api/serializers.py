from rest_framework import serializers
from booking.models import BookingInfomation
from core.custom_models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'full_name')


class BookingInfomationSerializer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format="%d/%m/%Y %H:%M", input_formats=['%d/%m/%Y'], required = True)
    user = UserSerializer(many=False)

    class Meta:
        model = BookingInfomation
        fields = ('order_id', 'order_desc', 'order_status', 'desc_transaction',
                  'barcode', 'amount', 'email', 'phone', 'created', 'user', 'poster')
