from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    friends = [
        'Gangoliya',
        'Gupta',
        'Pradhan',
        'Mishra',
    ]
    return JsonResponse(friends, safe = False)
 