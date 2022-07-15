from django.http import HttpResponse

class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initialization process view")
        # One time initialization

    def __call__(self, request):
        # code Runs before view
        print("code Runs before view")
        response = self.get_response(request) # calls next view/middleware
         # code Runs after view
        print("code Runs after view")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("Process View")
        # return HttpResponse("This is called just before view")
        return None

class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initialization")
        # One time initialization

    def __call__(self, request):
        # code Runs before view
        print("code Runs before exception view")
        response = self.get_response(request) # calls next view/middleware
         # code Runs after view
        print("code Runs after exception view")
        return response

    def process_exception(self, request, exception):
        print("Exception Occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(msg)
        print(f"Class Name : {class_name}")
        return HttpResponse(msg)