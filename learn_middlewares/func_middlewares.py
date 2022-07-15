
def function_middleware(get_response):
    print("One time Execution 111111111111111")

    def middleware(request):
        print("Code Before Another Middleware 111111111111111111")
        response = get_response(request)
        print("Code After Another Middleware 111111111111111111")
        
        return response

    return middleware

def function_middleware2(get_response):
    print("One time Execution 22222222222222")

    def middleware(request):
        print("Code Before View 22222222222222")
        response = get_response(request)
        print("Code After View 22222222222222222")
        
        return response

    return middleware