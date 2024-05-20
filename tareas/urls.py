from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_tarea_api, name='crear_tarea'),
    path('ver/<int:tarea_id>/', views.ver_tarea_api, name='ver_tarea'),
    path('editar/<int:tarea_id>/', views.editar_tarea_api, name='editar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea_api, name='eliminar_tarea'),
    path('listar/', views.listar_tareas, name='listar_tareas'),
]
