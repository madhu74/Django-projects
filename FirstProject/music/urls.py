from django.conf.urls import url
from . import views
app_name='music'

urlpatterns = [

url(r'^$',views.index,name='index'),

#adding second view
url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='details')
#r'^(?P<album_id>[0-9]+)/$'
]