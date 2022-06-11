from django.contrib import admin
from django.urls import path
from . views import index,uwus,service,about,contact,team,register,index2, escribir, agregar_producto, mypubli, listar, modificar, eliminar, otrapubli,com, regislis, modificaar, eliminaar, login, perfi, info

urlpatterns = [
    path('',index,name='index'),
    path('service/',service,name='service'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('team/',team,name='team'),
    path('register/',register,name='register'),
    path('index2/',index2,name='index2'),
    path('escribir/',escribir,name='escribir'),
    path('agregar/', agregar_producto, name='agregar'),
    path('mypubli/', mypubli, name='mypubli'),
    path('listar/', listar, name='listar'),
    path('modificar/<id>/', modificar, name='modificar'),
    path('eliminar/<id>/', eliminar, name='eliminar'),
    path('otrapubli/', otrapubli, name='otrapubli'),
    path('com/', com, name='com'),
    path('regislis/', regislis, name='regislis'),
    path('modificaar/<id>/', modificaar, name='modificaar'),
    path('eliminaar/<id>/', eliminaar, name='eliminaar'),
    path('login/',login, name='login'),
    path('perfi/',perfi, name='perfi'),
     path('info/',info, name='info'),
    path('uwu/',uwus,name='uwu')


]



    