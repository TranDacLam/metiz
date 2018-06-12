from django import forms


class MetizPaymentForm(forms.Form):
    total_payment = forms.IntegerField(min_value=1, disabled=True)
    working_id = forms.CharField(max_length=200, required=False, disabled=True)
    barcode = forms.CharField(max_length=50, required=False, disabled=True)
    seat_count = forms.IntegerField(required=False)
    seats = forms.CharField(max_length=1000, disabled=True)
    seats_choice = forms.CharField(max_length=1000, disabled=True)
    
    id_server = forms.IntegerField(required=False, disabled=True)
    id_showtime = forms.CharField(max_length=1000, disabled=True)
    movie_api_id = forms.CharField(max_length=1000, required=False, disabled=True)
    id_movie_name = forms.CharField(max_length=1000, required=False, disabled=True)
    id_movie_time = forms.CharField(max_length=200, required=False, disabled=True)
    id_movie_date_active = forms.CharField(max_length=200, required=False, disabled=True)
    

class MetizOTPForm(forms.Form):
    id_server = forms.IntegerField(required=True)
    order_id = forms.CharField(max_length=250)
    order_desc = forms.CharField(max_length=1000, required=False)
    barcode = forms.CharField(max_length=50, required=True)
    seats_choice = forms.CharField(max_length=1000, required=True)
    working_id = forms.CharField(max_length=200, required=True)
    card_barcode = forms.IntegerField(required=True)
    full_name = forms.CharField(max_length=500, required=False)
    payment_gate = forms.CharField(max_length=200, required=True)
    movie_poster = forms.CharField(max_length=500, required=False)
    phone_hide = forms.CharField(max_length=200, required=False)
    amount = forms.CharField(max_length=200, required=False)

    

# disabled
#         total_payment = data_json['totalPayment'] if 'totalPayment' in data_json else 0

#         seat_count = len(data_json['seats'])
#         seats_name = ','.join(data_json['seats']) 
#         seats = metiz_util.remove_uni(seats_name) if 'seats' in data_json else ""
#         working_id = data_json['working_id'] if 'working_id' in data_json else ""
#         barcode = data_json['barcode'] if 'barcode' in data_json else ""
#         # Handle list seats to string and remove unicode
#         seat_array = ','.join(data_json['seats_choice']) 
#         seats_choice = metiz_util.remove_uni(seat_array) if 'seats_choice' in data_json else ""
        
#         id_server = data_json['id_server'] if 'id_server' in data_json else 1
#         id_showtime = data_json['id_showtime'] if 'id_showtime' in data_json else ""
#         movie_api_id = data_json['movie_api_id'] if 'movie_api_id' in data_json else ""
#         id_movie_name = data_json['id_movie_name'] if 'id_movie_name' in data_json else ""
#         id_movie_time = data_json['id_movie_time'] if 'id_movie_time' in data_json else ""
#         id_movie_date_active = data_json['id_movie_date_active'] if 'id_movie_date_active' in data_json else ""