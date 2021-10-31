from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import HireForm
from django.views.generic import ListView, TemplateView
from hire.models import ItemforHire



def hire_form(request):
    if request.method == 'POST':
        form3 = HireForm(request.POST, request.FILES)

        if form3.is_valid():
            form3.save()
        return redirect('homepage')

    else:
        form3 = HireForm()
    return render(request, 'hire/hireform.html', {'form': form3})


