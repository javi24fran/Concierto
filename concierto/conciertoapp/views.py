from django.shortcuts import render
from conciertoapp.models import Entrada
from conciertoapp.forms import FormEntrada


def index (request):
    return render( request, 'conciertoapp/index.html')

def listarEntradas(request):
    entradas= Entrada.objects.all()
    data= {'entradas': entradas}
    return render (request, 'conciertoapp/entradas.html', data)

def agregarEntradas(request):
    form = FormEntrada()
    if request.method == 'POST':
        form = FormEntrada(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data= {'form': form}
    return render (request, 'conciertoapp/agregarentradas.html',data )

def eliminarProyecto(request, id):
    eliminar= Entrada.objects.get(id = id)
    eliminar.delete()
    return redirect ('/proyect')




# Create your views here.
