from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>Home Page for Music app</h1>")