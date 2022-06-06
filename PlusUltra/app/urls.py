from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    
    path('idiomas/<int:id>', views.idiomapub, name='idiomapub'),
    path('idiomas/<int:id>/add/', views.addidiomapub, name='addidiomapub'),
    path('genero/<int:id>/add/', views.addidiomapub, name='addidiomapub'),
    path('idiomas/<int:id>/delete/<int:id_idi>', views.deleteidiomapub, name='deleteidiomapub'),
    path('idiomas/<int:id>/update/<int:id_idi>', views.updateidiomapub, name='updateidiomapub'),

]
