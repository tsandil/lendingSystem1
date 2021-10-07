from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import ItemForm

def item_form(request):
    if request.method == 'POST':
        form2=ItemForm(request.POST, request.FILES)
        
        if form2.is_valid():
            form2.save()
            return HttpResponse("You have submitted item for selling!!!")
        
    else:
        form2=ItemForm()

    
    return render(request, 'sellItem/thirdpartyform.html',{'form2':form2})

   
   

