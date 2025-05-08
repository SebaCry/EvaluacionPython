from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductosForm

def home(request):
    productos = Producto.objects.all()
    context = {'productos' : productos}

    return render(request, 'productos/home.html', context)

def agregar(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    form = ProductosForm()

    context = {'form' : form}

    return render(request, 'productos/agregar.html', context)

def actualizar(request, id_prod):
    producto = Producto.objects.get(id=id_prod)

    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductosForm(instance=producto)

    context = {'form': form}
    return render(request, 'productos/actualizar.html', context)


def eliminar(request, id_prod):
    producto = Producto.objects.get(id=id_prod)
    producto.delete()
    return redirect('home')



# Create your views here.
