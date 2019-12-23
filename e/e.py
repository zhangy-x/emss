from django.http import HttpResponse


def index(request):
    print(222)

def login(request):
    return HttpResponse()


