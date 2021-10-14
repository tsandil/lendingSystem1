from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import HireForm
from django.views.generic import ListView, TemplateView
from hire.models import ItemforHire


def index1(request):
    prods1 = ItemforHire.objects.all()
    return render(request, 'hire/homePage.html', {'products': prods1})

def hire_form(request):
    if request.method == 'POST':
        form3 = HireForm(request.POST, request.FILES)

        if form3.is_valid():
            form3.save()
        return render(request, 'hire/hirePage.html', {})

    else:
        form3 = HireForm()
    return render(request, 'hire/hireform.html', {'form': form3})

def hirePage(request):
    return redirect('hirePage')

class HireItemListView(ListView):
     model = ItemforHire
     template_name = "hire/hirePage.html"
     context_object_name = "ads1"


class HirePageView(TemplateView):
     template_name='hirePage.html'


