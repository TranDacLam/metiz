from django import forms


class BookingForm(forms.Form):
	name = forms.CharField(max_length=250)
	phone = forms.IntegerField()
	email = forms.EmailField( required=False)
	id_server = forms.CharField()
	id_showtime = forms.CharField()
	movie_api_id = forms.CharField()
	id_movie_name = forms.CharField()
	id_movie_time = forms.CharField()
	id_movie_date_active = forms.CharField()

