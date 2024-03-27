
# from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse



def home_page(request):
    print("Home Page Requested")
    # return HttpResponse("<h1>This is home Page<h1>")
    friends=["Hira", "Hamna", "Sara"]
    return JsonResponse(friends, safe=False)