from rest_framework import serializers
from booking.models import BookingInfomation
import datetime
import time
import uuid
from core.metiz_cipher import MetizAESCipher


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
        return super(BookingInfomationSerializer, self).to_internal_value(data)
    
    # encrypt working_id to return Response
    def to_representation(self, instance):
        cipher = MetizAESCipher()
        instance.working_id = cipher.encrypt(str(instance.working_id))
        return super(BookingInfomationSerializer, self).to_representation(instance)
        

