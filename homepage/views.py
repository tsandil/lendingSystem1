from django.shortcuts import render
from django.http import HttpResponse

from lendingSystem1.settings import TEMPLATES
from homepage.models import Products
from sellItem.models import Item
from django.shortcuts import render
from django.views.generic import ListView, TemplateView


def index(request):
    
    prods=Products.objects.all()
    return render(request, 'homepage/index.html',{'products':prods})


class ItemListView(ListView):
    model = Item
    template_name = "homepage/index.html"
    context_object_name = "ads"


class HomePageView(TemplateView):
    template_name='index.html'

    
