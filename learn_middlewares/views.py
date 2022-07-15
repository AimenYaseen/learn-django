from django.shortcuts import render, HttpResponse

# Create your views here.
def func_middleware_view(request):
    print("I am in View")
    return HttpResponse("This is function base middleware...")