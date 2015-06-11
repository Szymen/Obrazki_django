from django.shortcuts import render
from models import Obrazek
def images_list(request):


    obrazki = Obrazek.objects.filter().order_by('id')
    return render(request, 'img_bro/image_list.html',{
        'obrazky' : obrazki
    })
