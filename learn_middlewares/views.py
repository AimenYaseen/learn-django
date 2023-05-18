from django.shortcuts import render, HttpResponse

# Create your views here.
def func_middleware_view(request):
    print("I am in View")
    return HttpResponse("This is function base middleware...")

def class_middleware_view(request):
    print("I am in class base middleware View")
    return HttpResponse("This is class base middleware...")

def exceptionView(request):
    print("This is Exception view")
    a = 10/0
    return HttpResponse("An Exception occurs in the view")