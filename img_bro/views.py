from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponseRedirect
from django import forms

from .forms import AddNewForm
from models import Obrazek

class ObrazekForm(forms.ModelForm):
    class Meta:
        model = Obrazek
form = ObrazekForm


def images_list(request):
    obrazki = Obrazek.objects.filter().order_by('id')
    if request.POST:
        wybrane = request.POST.getlist('kot')
        wszystkie_koty = Obrazek.objects.filter()
        for kotel_id in wybrane:
            wszystkie_koty[int(kotel_id)-1].glosuj()
            wszystkie_koty[int(kotel_id)-1].save()
    return render_to_response('img_bro/image_list.html',{'obrazky' : obrazki}, context_instance=RequestContext(request) )





def add_new(request):
    you_blind = "http://new4.fjcdn.com/thumbnails/comments/What+if+you+re+blind+_28fcfe83425a9bc22bfb3e77f3cd2617.jpeg"

    if request.POST:
        data = request.POST.copy()
        imie = data.__getitem__('nazwa')
        zrodlo = data.__getitem__('source')
        if Obrazek.objects.filter(nazwa=imie).count() == 0:
            new_cat = Obrazek( nazwa = imie, source = zrodlo )
            new_cat.save()
        if data:
            data.clear()
    return render_to_response(
		'img_bro/add_new.html',{'form':form},context_instance=RequestContext(request))