from datetime import datetime
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import cliente
from openpyxl import Workbook
from django.http.response import HttpResponse
# Create your views here.
class porfolioDash(TemplateView):
    template_name = 'cliente_dash.html'

class porfolioSearch(TemplateView):
    template_name = 'client_search.html'

class porfolioList(ListView):
    model = cliente

class porfolioDetail(DetailView):
    model = cliente

class porfolioCreated(CreateView):
    model = cliente
    success_url = reverse_lazy('porfolio:dash')
    fields = ['nombre', 'email', 'numeroT', 'descripcion']

class porfolioUpdate(UpdateView):
    model = cliente
    success_url = reverse_lazy('porfolio:list')
    fields = ['nombre', 'email', 'numeroT', 'descripcion']

class porfolioDetele(DeleteView):
    model = cliente
    success_url = reverse_lazy('porfolio:list')

#Nuestra clase hereda de la vista genérica TemplateView
class ReportePersonasExcel(TemplateView):
     
    #Usamos el método get para generar el archivo excel 
    def get(self, request, *args, **kwargs):
        #Obtenemos todas las personas de nuestra base de datos
        personas = cliente.objects.all()
        #Creamos el libro de trabajo
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'REPORTE DE PERSONAS'
        ws['B1'] = 'REPORTE DE PERSONAS'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:E1')
        #Creamos los encabezados desde la celda B3 hasta la E3
        ws['B3'] = 'nombre'
        ws['C3'] = 'correo electronico'
        ws['D3'] = 'numero de telefono'
        ws['E3'] = 'descripcion'       
        cont=4
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for persona in personas:
            ws.cell(row=cont,column=2).value = persona.nombre
            ws.cell(row=cont,column=3).value = persona.email
            ws.cell(row=cont,column=4).value = persona.numeroT
            ws.cell(row=cont,column=5).value = persona.descripcion
            cont = cont + 1
        #Establecemos el nombre del archivo
        nombre_archivo ="ReportePersonasExcel.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        response = HttpResponse(content_type="application/ms-excel") 
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response