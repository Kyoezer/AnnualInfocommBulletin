from django.shortcuts import render
from .models import *


def home(request):
    usertypes = UserTypes.objects.all()
    dzongkhags = Dzongkhag.objects.all()
    context = {'usertypes': usertypes,
               'dzongkhags': dzongkhags,
               }
    return render(request, 'base/home.html', context)

