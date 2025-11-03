
from django.http import HttpResponse

def property_list(request):
    return HttpResponse("available properties")

