import sqlite3
from xml.dom.minidom import Document
from django.http import HttpResponse
import pathlib
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

from Familiares.models import Familiar


path = pathlib.Path(__file__).parent.resolve()

def home(self):
    return HttpResponse('''
    Bienvenido a HomeFamiliy
    Para ver la template escribe "/template/" al final del url
    Para ver los familiares escribe "/famialiares/" al final de la url
    ''')

def template(self):
    planilla = loader.get_template('index.html')
    documento = planilla.render()
    return HttpResponse(documento)

def familiares(self):
    Familia = []
    familiar1 = Familiar(nombre='Diego',apellido='Rindispager',edad=22,fechaDeNac='1980-05-22')
    familiar1.save()
    Familia.append(familiar1)
    familiar2 = Familiar(nombre='Agustina',apellido='Toledo',edad=13,fechaDeNac='2009-05-5')
    familiar2.save()
    Familia.append(familiar2)
    familiar3 = Familiar(nombre='Sofia',apellido='Toledo',edad=13,fechaDeNac='2009-08-5')
    familiar3.save()
    Familia.append(familiar3)
    data = {'lista':Familia}
    planilla = loader.get_template('familiares.html')
    documento = planilla.render(data)
    return HttpResponse(documento)
    
def listaFamiliares(request):
    familiares = Familiar.objects.all()
    return render(request,'lista.html',{'lista':familiares})