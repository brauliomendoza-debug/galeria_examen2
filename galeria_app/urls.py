from django.urls import path
from . import views

urlpatterns = [

    path('album/', views.AlbumList.as_view(), name='album_list'),
    path('album/nuevo/', views.AlbumCreate.as_view(), name='album_create'),
    path('album/editar/<int:pk>/', views.AlbumUpdate.as_view(), name='album_update'),
    path('album/eliminar/<int:pk>/', views.AlbumDelete.as_view(), name='album_delete'),
    path('album/<int:pk>/', views.AlbumDetail.as_view(), name='album_detail'),

   
    path('foto/', views.FotoList.as_view(), name='foto_list'),
    path('foto/nuevo/<int:album_id>/', views.FotoCreate.as_view(), name='foto_create_album'),
    path('foto/editar/<int:pk>/', views.FotoUpdate.as_view(), name='foto_update'),
    path('foto/eliminar/<int:pk>/', views.FotoDelete.as_view(), name='foto_delete'),
]