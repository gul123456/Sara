from django.conf.urls import url
from . import views
app_name='music'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    #/music/album_id/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    #/music/album_id/favourite/ 
    url(r'album/add/$',views.AddAlbum.as_view(),name = 'add_album'),

    url(r'album/(?P<pk>[0-9]+)/$',views.UpdateAlbum.as_view(),name = 'update_album'),

    url(r'album/(?P<pk>[0-9]+)/delete/$',views.DeleteAlbum.as_view(),name = 'delete_album'),
]
