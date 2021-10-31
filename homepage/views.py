# from django.shortcuts import render
# from django.http import HttpResponse

from lendingSystem1.settings import TEMPLATES
from homepage.models import Products
from sellItem.models import Item
from django.views.generic import ListView, TemplateView
from hire.models import ItemforHire

# class ItemListView(ListView):
#     model = Item
#     template_name = "homepage/index.html"
#     context_object_name = "ads"

class IndexView(ListView):
    context_object_name = 'home_list'    
    template_name = 'homepage/index.html'
    queryset = Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['ads'] = Item.objects.all()
        context['ads1'] = ItemforHire.objects.all()
        return context

class HomePageView(TemplateView):
    template_name='index.html'

    
