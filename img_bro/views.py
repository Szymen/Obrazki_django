from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddNewForm
from models import Obrazek


def images_list(request):

    obrazki = Obrazek.objects.filter().order_by('id')
    return render(request, 'img_bro/image_list.html',{
        'obrazky' : obrazki
    })


#def vote(request,new_name,new_source):
#    return render(request, 'img_bro/add_new.html',{})


def add_new(request):
    return render(request,'img_bro/add_new.html', {'form' : AddNewForm})

def added_new(request):
    if request.method == 'POST':
        form = AddNewForm(request.POST)
        if form.is_valid():
            imie = form.cleaned_data['new_name']
            zrodlo = form.cleaned_data['new_source']
            new_cat = Obrazek( nazwa = imie, source = zrodlo )
            new_cat.save()
            return HttpResponseRedirect('/add_new')
    return HttpResponseRedirect("/add_new")
