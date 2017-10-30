from django import forms


class BookingForm(forms.Form):
	name = forms.CharField(max_length=250)
	phone = forms.IntegerField()
	email = forms.EmailField( required=False)
	id_showtime = forms.CharField()

