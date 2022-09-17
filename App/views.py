from django.shortcuts import render
from . import models


def home(request):
    return render(request, 'home.html')


def donation(request):
    return render(request, 'donations.html')


def gallery(request):
    photos = models.Gallery.objects.all()
    return render(request, 'gallery.html', {'Photos': photos})


def volunteers(request):
    return render(request, 'volunteers.html')
