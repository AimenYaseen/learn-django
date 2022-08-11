from django.http import HttpResponse
from json import dumps
import requests

def index(request):
    myip = requests.get('https://httpbin.org/ip')
    return HttpResponse(myip)