#Configurando redireccionamiento 
from django.urls import path
from . import views
urlpatterns = [
     path('',views.home),
     path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),
     path('listadoPelicula/',views.listadoPelicula, name='listadoPelicula'),
     path('listadoPais/', views.listadoPais, name='listadoPais'),
     path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
     path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
     path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
     path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
     path('procesarActualizacionGenero/',views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
     path('editarDirector/<id>',views.editarDirector, name='editarDirector'),
     path('procesarActualizacionDirector/',views.procesarActualizacionDirector, name='procesarActualizacionDirector'),
     path('editarPais/<id>',views.editarPais, name='editarPais'),
     path('procesarActualizacionPais/',views.procesarActualizacionPais, name='procesarActualizacionPais'),
     path('editarPelicula/<id>',views.editarPelicula, name='editarPelicula'),
     path('procesarActualizacionPelicula/',views.procesarActualizacionPelicula, name='procesarActualizacionPelicula'),
     path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
     path('guardarDirector/',views.guardarDirector, name='guardarDirector'),
     path('eliminarDirector/<id>',views.eliminarDirector, name='eliminarDirector'),
     #CINES
     path('gestionCines/',views.gestionCines, name='gestionCines'), 
     path('guardarCine/',views.guardarCine, name='guardarCine'), 
     path('listadoCines/',views.listadoCines, name='listadoCines'), 
     #DIRECTORES
     path('gestionDirectores/',views.gestionDirectores, name='gestionDirectores'), 
     path('guardarDirector/',views.guardarDirector, name='guardarDirector'), 
     path('listadoDirectores/',views.listadoDirectores, name='listadoDirectores'), 
     #PELICULAS
     path('gestionPeliculas/',views.gestionPeliculas, name='gestionPeliculas'), 
     path('guardarPelicula/',views.guardarPelicula, name='guardarPelicula'), 
     path('listadoPeliculas/',views.listadoPeliculas, name='listadoPeliculas'),
     
]
