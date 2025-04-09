from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('nueva/', views.crear_receta, name='crear_receta'),
    path('receta/<int:receta_id>/editar/', views.editar_receta, name='editar_receta'),
    path('receta/<int:receta_id>/eliminar/', views.eliminar_receta, name='eliminar_receta'),
    path('categoria/<int:categoria_id>/', views.recetas_por_categoria, name='recetas_por_categoria'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),

]   
