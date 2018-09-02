from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
from django.template import  RequestContext

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

    return HttpResponse("We are analizing your request. Please wait a moment. This process will use your geographic location. Your ip is" + str(ip))

    g = GeoIP2()
    city = g.city(ip)

    return HttpResponse("Teste cidade " + city)




