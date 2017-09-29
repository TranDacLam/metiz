# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from datetime import *

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

def custom_404(request):
	return render(request, 'websites/errors/404.html', {}, status=404)

def custom_500(request):
	return render(request, 'websites/errors/500.html', {}, status=500)

def showing(request):
	try:
		data_modal= data_schedule
		sql = 'SELECT * FROM core_movie Where release_date <= now()'
		data_showing = Movie.objects.raw(sql)
		genre = Genre.objects.all()
		movieType = MovieType.objects.all()
		rateds = Rated.objects.all()
		return render(request, 'websites/showing.html', {'data_showing':data_showing,'genre':genre,'movieType':movieType,'rateds':rateds, 'data_modal': data_modal, 'last' : range(15,27),'present': range(27,30), 'future': range(1,15)})
	except Exception, e:
		print "Error: ", e
		raise Exception(
			"ERROR : Internal Server Error .Please contact administrator.")

def comingsoon(request):	
	try:
		data_modal= data_schedule
		sql = 'SELECT * FROM core_movie Where release_date > now()'
		data = Movie.objects.raw(sql)
		genre = Genre.objects.all()
		movieType = MovieType.objects.all()
		rateds = Rated.objects.all()
		return render(request, 'websites/coming_soon.html', {'data':data ,'genre':genre, 'movieType':movieType,'rateds':rateds, 'data_modal': data_modal, 'last' : range(15,27),'present': range(27,30), 'future': range(1,15)})
	except Exception, e:
		print "Error: ", e
		raise Exception(
			"ERROR : Internal Server Error .Please contact administrator.")

def film_detail(request, id):	
	try:
		data_modal= data_schedule
		film_detail = Movie.objects.get(pk=id)
		genre = Genre.objects.all()
		movieType = MovieType.objects.all()
		rateds = Rated.objects.all()
		return render(request, 'websites/film_detail.html', {'film_detail': film_detail,'genre':genre,'movieType':movieType, 'rateds':rateds, 'data_modal': data_modal, 'last' : range(15,27),'present': range(27,30), 'future': range(1,15)})
	except Exception, e:
    		print "Error: ", e
    	raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.") 