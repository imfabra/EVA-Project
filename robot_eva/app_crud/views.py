from django.shortcuts import render, get_object_or_404, redirect
from .models import Etiqueta, Movimiento, Submovimiento
from .forms import EtiquetaForm, MovimientoForm, SubmovimientoForm



########################################################################
def etiqueta_list(request):
    etiquetas = Etiqueta.objects.all()
    movimientos = Movimiento.objects.all()
    submovimientos = Submovimiento.objects.all()
    #return render(request, 'app_crud/etiqueta_list.html', {'etiquetas': etiquetas})
    return render(request, 'app_crud/index.html', {'etiquetas': etiquetas, 'movimientos': movimientos, 'submovimientos': submovimientos})

def etiqueta_detail(request, etiqueta_id):
    etiqueta = get_object_or_404(Etiqueta, id=etiqueta_id)
    return render(request, 'app_crud/etiqueta_detail.html', {'etiqueta': etiqueta})

def etiqueta_create(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_list')
    else:
        form = EtiquetaForm()
    return render(request, 'app_crud/etiqueta_create.html', {'form': form})

def etiqueta_update(request, etiqueta_id):
    etiqueta = get_object_or_404(Etiqueta, id=etiqueta_id)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_list')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'app_crud/etiqueta_update.html', {'form': form, 'etiqueta': etiqueta})

def etiqueta_delete(request, etiqueta_id):
    etiqueta = get_object_or_404(Etiqueta, id=etiqueta_id)
    etiqueta.delete()
    return redirect('etiqueta_list')



# ----------------------------------------------------------------

def movimiento_list(request):
    movimientos = Movimiento.objects.all()
    return render(request, 'app_crud/movimiento_list.html', {'movimientos': movimientos})

def movimiento_detail(request, movimiento_id):
    movimiento = get_object_or_404(Movimiento, id=movimiento_id)
    return render(request, 'app_crud/movimiento_detail.html', {'movimiento': movimiento})

def movimiento_create(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movimiento_list')
    else:
        form = MovimientoForm()
    return render(request, 'app_crud/movimiento_create.html', {'form': form})

def submovimiento_list(request):
    submovimientos = Submovimiento.objects.all()
    return render(request, 'app_crud/submovimiento_list.html', {'submovimientos': submovimientos})

def submovimiento_detail(request, submovimiento_id):
    submovimiento = get_object_or_404(Submovimiento, id=submovimiento_id)
    return render(request, 'app_crud/submovimiento_detail.html', {'submovimiento': submovimiento})

def submovimiento_create(request):
    if request.method == 'POST':
        form = SubmovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submovimiento_list')
    else:
        form = SubmovimientoForm()
    return render(request, 'app_crud/submovimiento_create.html', {'form': form})
