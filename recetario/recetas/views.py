from django.shortcuts import redirect, render, get_object_or_404

from .forms import RecetaForm
from .models import Categoria, Receta



def lista_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_creacion')
    categorias = Categoria.objects.all()
    return render(request, 'recetas/lista_recetas.html', {
        'recetas': recetas,
        'categorias': categorias,
    })


def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'recetas/detalle_receta.html', {'receta': receta})


def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas/crear_receta.html', {'form': form})

def editar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('detalle_receta', receta_id=receta.id)
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'recetas/editar_receta.html', {'form': form, 'receta': receta})

def eliminar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        receta.delete()
        return redirect('lista_recetas')
    return render(request, 'recetas/eliminar_receta.html', {'receta': receta})



def recetas_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    recetas = Receta.objects.filter(categoria=categoria).order_by('-fecha_creacion')
    return render(request, 'recetas/recetas_por_categoria.html', {
        'categoria': categoria,
        'recetas': recetas
    })

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'recetas/lista_categorias.html', {'categorias': categorias})

def buscar_recetas(request):
    query = request.GET.get('q', '')
    recetas = Receta.objects.filter(titulo__icontains=query) if query else Receta.objects.all()
    return render(request, 'recetas/buscar_recetas.html', {'recetas': recetas, 'query': query})
