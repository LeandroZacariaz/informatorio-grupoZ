
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),

	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
    
    path('Comentario/eliminar/<int:pk>', views.eliminar_comentario, name = 'eliminar_comentario'),
    
	path('Comentario/editar/<int:pk>', views.modificar_comentario, name = 'modificar_comentario')
	
]