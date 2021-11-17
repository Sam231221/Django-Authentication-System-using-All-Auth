from django.shortcuts import render
from django.views.generic import TemplateView


def HomeView(request):

     context={

     }
     return render(request, 'frontendbase.html', context)

     
