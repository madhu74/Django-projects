from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>Home Page for Music app</h1>")

def detail(response,album_id):
    return HttpResponse("<h1>Accessing album id "+str(album_id)+"</h1>")