from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import MusicEvents

# Create your views here.


def index(request):
	template = loader.get_template('events/index.html')
	context = {}
	return HttpResponse(template.render(context, request))


def mainMap(request):
	# zapytania do bazy danych
	all_events = MusicEvents.objects.all()
	distinct_city = MusicEvents.objects.values('city').distinct()
	distinct_country = MusicEvents.objects.values('country').distinct()
	distinct_band = MusicEvents.objects.values('artist').distinct()

	template = loader.get_template('events/mainMap.html')
	context = {
		'all_events' : all_events, 'distinct_city' : distinct_city,
		'distinct_country' : distinct_country, 'distinct_band' : distinct_band,
	}
	return HttpResponse(template.render(context, request))


def listOfEvents(request):
	all_events = MusicEvents.objects.all()
	template = loader.get_template('events/listOfEvents.html')
	context = {
		'all_events' : all_events,
	}
	return HttpResponse(template.render(context, request))


def detailsView(request, category, value):
	all_events = MusicEvents.objects.all()
	categoryList = ['band', 'city', 'country']
	template = loader.get_template('events/subsetDetails.html')
	context = {
		'category' : category, 'value' : value,
		'data' : all_events, 'categoryList' : categoryList,
	}
	return HttpResponse(template.render(context, request))