from django.shortcuts import render
from django.http import HttpResponse

from lendingSystem1.settings import TEMPLATES
from homepage.models import Products
from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    prods=Products.objects.all()
    return render(request, 'homepage/index.html',{'products':prods})


class HomePageView(TemplateView):
    template_name='index.html'

    
