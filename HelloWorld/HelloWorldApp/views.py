# Create your views here.
from django.http import HttpResponse
def foo(request):
    return HttpResponse("Hello World!")

