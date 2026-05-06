from django.db import models

class Album(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)  
    portada = models.ImageField(upload_to='albumes/')  

    def __str__(self):
        return self.nombre


class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to='fotos/')  
    fecha = models.DateField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  

    def __str__(self):
        return self.titulo