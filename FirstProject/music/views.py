from django.http import HttpResponse
from django.http import Http404
from . models import Album
from django.shortcuts import render
from django.template import loader

# def index(response):
#     html_tag=""
#
#     for album in Album.objects.all():
#         url="/music/"+str(album.id)+"/"
#         html_tag+='<a href="'+ url +'">'+album.album_name+"</a><br>"
#
#     return HttpResponse(html_tag)

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))

def detail(request,album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.ObjectDoesNotExist:
        raise Http404("Album does not exist")

    return render(request,'music/detail.html',{'album' : album, })