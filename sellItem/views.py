from django.shortcuts import render, redirect
from .forms import ItemForm

def item_form(request):
    if request.method == 'POST':
        form2=ItemForm(request.POST)


        if form2.is_valid():
            form2.save()
            return render(request,'sellItem/itemadd.html')
        
        else:
            form2=ItemForm()
            return render(request, 'sellItem/thirdpartyform.html',{'form':form2})


