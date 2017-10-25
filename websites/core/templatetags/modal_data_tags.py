from django import template
from datetime import date, timedelta
from django.http import JsonResponse

register = template.Library()
@register.filter(name='get_data_modal')
def get_data_modal(value):
	data_schedule= [{
	'date':'2017-10-27',
	'film':[
		{'name': 'Yeu Di Dung So',
		'schedule': [
		{'from': '8:35', 'to': '10:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '21:35', 'to': '0:35', 'room': 119,'name_room': 'Scm01'},
		] },
		{'name': 'The gioi nay la cua bo may',
		'schedule': [
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		] },
		{'name': 'Chu he IT',
		'schedule': [
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		]}
	]},
	{
	'date':'2017-10-28',
	'film':[
		{'name': 'Yeu Di Dung So',
		'schedule': [
		{'from': '8:35', 'to': '10:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		
		] },
		{'name': 'The gioi nay la cua bo may',
		'schedule': [
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		] },
		{'name': 'Chu he IT',
		'schedule': [
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		]}
	]},
	{
	'date':'2017-10-29',
	'film':[
		{'name': 'Yeu Di Dung So',
		'schedule': [
		{'from': '8:35', 'to': '10:35', 'room': 119,'name_room': 'Scm01'},
		
		] },
		{'name': 'The gioi nay la cua bo may',
		'schedule': [
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '21:35', 'to': '0:35', 'room': 119,'name_room': 'Scm01'},
		] },
		{'name': 'Chu he IT',
		'schedule': [
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		{'from': '18:35', 'to': '21:35', 'room': 119,'name_room': 'Scm01'},
		]}
	]},
	]
	data_cinema = {'danang':['Metiz Cinema'],
	'hanoi':['Metiz Cinema 1', 'Metiz Cinema 2'],
	'hcm':['Metiz Cinema']
	}
	data_celendar = {'last' : range(15,27),'present':range(27,30), 'future': range(1,15) }
	return {'data_schedule': data_schedule, 'data_celendar':data_celendar, 'data_cinema': data_cinema}


@register.filter
def floatdot(value, decimal_pos=4):
    return format(value, '.%if'%decimal_pos)


floatdot.is_safe = True
