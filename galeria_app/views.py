from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Album, Foto
from django.urls import reverse_lazy


class AlbumList(ListView):
    model = Album

class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'
    template_name = 'galeria_app/form.html'
    success_url = reverse_lazy('album_list')

class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__'
    template_name = 'galeria_app/form.html'
    success_url = reverse_lazy('album_list')

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'galeria_app/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')

class AlbumDetail(DetailView):
    model = Album


class FotoList(ListView):
    model = Foto


class FotoCreate(CreateView):
    model = Foto
    fields = ['titulo', 'archivo']  
    template_name = 'galeria_app/form.html'

    def form_valid(self, form):
        album_id = self.kwargs.get('album_id')
        form.instance.album_id = album_id  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('album_detail', kwargs={'pk': self.object.album.id})
  


class FotoUpdate(UpdateView):
    model = Foto
    fields = ['titulo', 'archivo']  
    template_name = 'galeria_app/form.html'

    def get_success_url(self):
        return reverse_lazy('album_detail', kwargs={'pk': self.object.album.id})
       

class FotoDelete(DeleteView):
    model = Foto
    template_name = 'galeria_app/foto_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('album_detail', kwargs={'pk': self.object.album.id})