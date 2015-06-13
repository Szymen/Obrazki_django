from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponseRedirect
from django import forms

from .forms import AddNewForm
from models import Obrazek

def images_list(request):

    obrazki = Obrazek.objects.filter().order_by('id')
    return render(request, 'img_bro/image_list.html',{
        'obrazky' : obrazki
    })


#def vote(request,new_name,new_source):
#    return render(request, 'img_bro/add_new.html',{})

class ObrazekForm(forms.ModelForm):
    class Meta:
        model = Obrazek



def add_new(request):
    you_blind = "http://new4.fjcdn.com/thumbnails/comments/What+if+you+re+blind+_28fcfe83425a9bc22bfb3e77f3cd2617.jpeg"
    form = ObrazekForm
    if request.POST:
        data = request.POST.copy()
        imie = data.__getitem__('nazwa')
        zrodlo = data.__getitem__('source')
        new_cat = Obrazek( nazwa = imie, source = zrodlo )
        if new_cat.nazwa != "":
            new_cat.save()
    return render_to_response(
		'img_bro/add_new.html',{'form':form},context_instance=RequestContext(request))