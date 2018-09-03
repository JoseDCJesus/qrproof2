from django.shortcuts import render
from django.http import HttpResponse, Http404
#from django.contrib.gis.geoip2 import GeoIP2
from django.template import  RequestContext
from geopy.geocoders import Nominatim
import pygeoip


from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the QRProof homepage")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def check(request, product_id):

    ip = get_client_ip(request)

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist ahaahah")

    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(product.sale_place)

    #return HttpResponse("We are analizing your request. Please wait a moment. This process will use your geographic location. Your ip is " + str(ip))
    g = pygeoip.GeoIP('GeoLite2-City.mmdb')

    city_lat = g.record_by_addr(str(ip))['latitude']
    city_log = g.record_by_addr(str(ip))['longitude']

    if ( (abs(city_lat - location.latitude) <= 1) and ( abs(city_log - location.longitude) <= 0.3 ) ):
        return Httpresponse( "O produto " + str(product.product_name) + " é autêntico  e originário de " + str(product.product_origin) )
    else:
        return HttpResponse("O produto é falsificado ")

    return HttpResponse("Teste cidade " + city)




