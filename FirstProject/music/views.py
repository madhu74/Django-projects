from django.http import HttpResponse
from . models import Album

def index(response):
    html_tag=""

    for album in Album.objects.all():
        url="/music/"+str(album.id)+"/"
        html_tag+='<a href="'+ url +'">'+album.album_name+"</a><br>"

    return HttpResponse(html_tag)

def detail(response,album_id):
    return HttpResponse("<h1>Details of album id :"+str(album_id)+"</h1>")