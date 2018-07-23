from rest_framework import serializers


class PaymentSerializers(serializers.Serializer):
    id_server = serializers.IntegerField(required=True)
    order_id = serializers.CharField(max_length=250)
    order_desc = serializers.CharField(max_length=1000, required=False)
    barcode = serializers.CharField(max_length=50, required=True)
    seats_choice = serializers.CharField(max_length=1000, required=True)
    working_id = serializers.CharField(max_length=200, required=True)
    card_barcode = serializers.IntegerField(required=True)
    full_name = serializers.CharField(max_length=500, required=False)
    payment_gate = serializers.CharField(max_length=200, required=True)
    amount = serializers.CharField(max_length=200, required=False)
