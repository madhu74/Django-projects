from django.http import HttpResponse

def mindex(response):
    return HttpResponse("<h1>Main Page<\h1>")
