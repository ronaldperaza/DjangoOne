from django.urls import path
from .views import *

urlpatterns = [
   path('',home, name= 'index'),
   path('generales', generales, name= 'generales'),
   path('programacion', programacion, name= 'programacion'),
   path('tecnologia', tecnologia, name= 'tecnologia'),
   path('videojuegos', videojuegos, name= 'videojuegos'),
   # path('tutoriales', tutoriales, name= 'tutoriales'),
   # path('contacto', contacto, name= 'contacto'),
   path('<slug:slug>/', detallePost, name= 'detalle_post'),  #signo mayor nombre para ver url
]
