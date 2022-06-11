from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class postis(models.Model):
    
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField()
    def __str__(self):
        return self.author

class comment (models.Model):
    postis= models.ForeignKey(postis, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    content = models.CharField(max_length=225)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.postis.title

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    sujeto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario

class Publis(models.Model):
    Publicacion=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class uwu(models.Model):
    usuario = models.CharField(max_length=50)
    publiuwu = models.CharField(max_length=500)  

    def __str__(self):
        return self.usuario   

class publicacionn(models.Model):
    
    nombre = models.CharField(max_length=50)
    sujeto = models.CharField(max_length=50)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre

class otrapubli(models.Model):
    nombre = models.CharField(max_length=50)
    sujeto = models.CharField(max_length=50)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre

class comentario(models.Model):
    nombre = models.CharField(max_length=50)
    mensaje = models.TextField()
    def __str__(self):
        return self.nombre

class login(models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario