import sqlite3
from django.http import HttpResponse
import pathlib
from django.template import Template, Context
from django.template import loader

from Familiares.models import Familiar


path = pathlib.Path(__file__).parent.resolve()

def home(self):
    return HttpResponse('''
    Bienvenido a HomeFamiliy
    Para ver la template escribe "/template/" al final del url
    Para ver los familiares escribe "/famialiares/" al final de la url
    ''')

def template(self):
    familiares = [
        {
    'nombre':'Damian','nroFavorito':'19','fechaDeNac':'16/02/1969'
    },
    {
    'nombre':'Matias','nroFavorito':'1','fechaDeNac':'25/10/1999'
    },
    {
    'nombre':'Agustina','nroFavorito':'7','fechaDeNac':'21/05/2009'
    }
    ]
    data = {'lista':familiares}
    planilla = loader.get_template('index.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def familiares(self):
    familiar1 = Familiar(nombre='Diego',apellido='Rindispager',edad=22,fechaDeNac='1980-05-22')
    familiar1.save()
    familiar2 = Familiar(nombre='Agustina',apellido='Toledo',edad=13,fechaDeNac='2009-05-5')
    familiar2.save()
    familiar3 = Familiar(nombre='Sofia',apellido='Toledo',edad=13,fechaDeNac='2009-08-5')
    familiar3.save()
    documento1 = f'{familiar1.nombre} {familiar1.apellido} tiene {familiar1.edad} años porque nacio el {familiar1.fechaDeNac}'
    documento2 = f'{familiar2.nombre} {familiar2.apellido} tiene {familiar2.edad} años porque nacio el {familiar2.fechaDeNac}'
    documento3 = f'{familiar3.nombre} {familiar3.apellido} tiene {familiar3.edad} años porque nacio el {familiar3.fechaDeNac}'
    return HttpResponse(documento1)
