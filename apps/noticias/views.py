from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

from .models import Noticia, Categoria, Comentario

from django.urls import reverse_lazy

def Listar_Noticias(request):
    contexto = {}

    id_categoria = request.GET.get('id', None)
    orden_asc = request.GET.get('orden_asc', None)
    orden_desc = request.GET.get('orden_desc', None)
    fecha_asc = request.GET.get('fecha_asc', None)
    fecha_desc = request.GET.get('fecha_desc', None)

    if id_categoria:
        noticias = Noticia.objects.filter(categoria_noticia=id_categoria)
    else:
        noticias = Noticia.objects.all()

    # Ordenar alfabéticamente asc si se proporciona el parámetro "orden"
    if orden_asc == 'alfabetico':
        noticias = noticias.order_by('titulo')  # Asume que el campo de título es 'titulo'
        
	# Ordenar alfabéticamente descendentemente
    if orden_desc == 'alfabetico':
        noticias = noticias.order_by('-titulo')  # El guion antes de 'titulo' indica orden
    
	# Ordenar por fecha ascendentemente
    if fecha_asc == 'fecha':
        noticias = noticias.order_by('fecha')  # El guion antes de 'titulo' indica orden 
	# Ordenar por fecha descendentemente
    if fecha_desc == 'fecha':
        noticias = noticias.order_by('-fecha')  # El guion antes de 'titulo' indica orden
    
    contexto['noticias'] = noticias

    categorias = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = categorias

    return render(request, 'noticias/listar.html', contexto)



def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

@login_required
def eliminar_comentario(request, pk):
     com = Comentario.objects.get(pk = pk)
     com.delete()
     return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': com.noticia.id}))

@login_required
def modificar_comentario(request, pk):
    comentario=request.POST.get('comentarioedit', None)
    com = Comentario.objects.get(pk = pk)
    com.texto = comentario
    com.save()
    return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': com.noticia.id}))



#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''