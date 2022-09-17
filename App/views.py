from django.shortcuts import render
from django.contrib import messages
from . import models
import datetime as T

x = T.datetime.now()
todayDate = x.strftime('%Y-%m-%d')
timeNow = x.strftime('%I:%M:%S %p')


def home(request):
    gallery = models.Gallery.objects.all()
    voluntreers = models.Volunteer.objects.all()
    projects = models.Volunteer.objects.all()
    return render(request, 'home.html', {'gallery': gallery, 'volunteer': voluntreers, 'projects': projects})


def donation(request):
    return render(request, 'donations.html')


def gallery(request):
    photos = models.Gallery.objects.all()
    return render(request, 'gallery.html', {'Photos': photos})


def volunteers(request):
    data = models.Volunteer.objects.all()
    return render(request, 'volunteers.html', {'vulData': data})


def volunteer_profile(request, id):
    data = models.Volunteer.objects.filter(id=id)
    return render(request, 'volunteer-profile.html', {'vulProfile': data})


def projects(request):
    data = models.Project.objects.all()
    return render(request, 'projects.html', {'proData': data})


def project_detail(request, id):
    data = models.Project.objects.filter(id=id)
    return render(request, 'project-details.html', {'proDetails': data})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name').title()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message').title()
        models.Contact(Name=name, Email=email, Phone=phone, Message=message, Date=todayDate, Time=timeNow).save()
        messages.success(request, "Your Message Has Been Sended Successfully")
    return render(request, 'contact.html')
