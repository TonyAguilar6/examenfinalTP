from django.shortcuts import render, redirect

from .models import *
# Create your views here.



def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        date_bo = request.POST.get('date_bo')
        telefono = request.POST.get('telefono')
        direcciono = request.POST.get('direcciono')
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        ram = request.POST.get('ram')
        rom = request.POST.get('rom')

        model_employee = employee(name=name,
                                lastname=lastname,
                                date_bo=date_bo,
                                telefono=telefono,
                                direcciono=direcciono,
                                  modelo=modelo,
                                  marca=marca,
                                  ram=ram,
                                  rom=rom)

        model_employee.save()
        return redirect('webprogra:index')

    elif request.method == "GET":
        return render(request, 'index.html')

def tablas(request):
    allemployee = employee.objects.all()
    return render(request, 'tablas.html', {'allemployee': allemployee})

def updateEmpleado(request, pk_employee):
    print('esta es la  pk: ', pk_employee)
    model_employee = employee.objects.get(pk_employee=pk_employee)
    if request.method == "POST":
        model_employee.name = request.POST.get('name')
        model_employee.lastname = request.POST.get('lastname')
        model_employee.date_bo = request.POST.get('date_bo')
        model_employee.telefono = request.POST.get('telefono')
        model_employee.direcciono = request.POST.get('direcciono')
        model_employee.modelo = request.POST.get('modelo')
        model_employee.marca = request.POST.get('marca')
        model_employee.ram = request.POST.get('ram')
        model_employee.rom = request.POST.get('rom')
        model_employee.save()
        return redirect('webprogra:tablas')
    return render(request, 'index.html', {'employee':model_employee})
def deleteEmpleado(request, pk_employee):
    model_employee = employee.objects.get(pk_employee=pk_employee)
    model_employee.delete()
    return redirect('webprogra:tablas')