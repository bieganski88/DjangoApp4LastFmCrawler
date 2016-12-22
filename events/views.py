"""
@author: Przemyslaw Bieganski, bieg4n@gmail.com
"""
#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import MusicEvents

# Create your views here.


def index(request):
    """Start page."""
    template = loader.get_template('events/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def about(request):
    """About page"""
    template = loader.get_template('events/about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def main_map(request):
    """Main map - display all features"""
	# database queries
    all_events = MusicEvents.objects.all()
    distinct_city = MusicEvents.objects.values('city').distinct().order_by('city')
    distinct_country = MusicEvents.objects.values('country').distinct().order_by('country')
    distinct_band = MusicEvents.objects.values('artist').distinct().order_by('artist')
    distinct_place = MusicEvents.objects.values('place').distinct().order_by('place')

    template = loader.get_template('events/mainMap.html')
    context = {
        'all_events' : all_events, 'distinct_city' : distinct_city,
        'distinct_country' : distinct_country, 'distinct_band' : distinct_band,
        'distinct_place' : distinct_place,}
    return HttpResponse(template.render(context, request))


def list_of_events(request):
    """Table with all events"""
    all_events = MusicEvents.objects.all()
    template = loader.get_template('events/listOfEvents.html')
    context = {
        'all_events' : all_events,
        }
    return HttpResponse(template.render(context, request))


def details_view(request, category, value):
    """Map - selection view."""
    all_events = MusicEvents.objects.all()
    category_list = ['band', 'city', 'country', 'place', 'byDate']
    template = loader.get_template('events/subsetDetails.html')
    context = {'category' : category, 'value' : value, 'data' : all_events,
               'category_list' : category_list,
              }
    return HttpResponse(template.render(context, request))
