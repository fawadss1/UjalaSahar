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
    return render(request, 'Home.html', {'gallery': gallery, 'volunteers': voluntreers, 'projects': projects})


def events(request):
    data = models.Event.objects.all()
    return render(request, 'Events.html', {'EventData': data})


def eventDetails(request, evnid):
    data = models.Event.objects.filter(id=evnid)
    return render(request, 'Event-Details.html', {'EventData': data})


def projects(request):
    data = models.Project.objects.all()
    return render(request, 'Projects.html', {'proData': data})


def projectDetails(request, proid):
    data = models.Project.objects.filter(id=proid)
    return render(request, 'Project-Details.html', {'proDetails': data})


def volunteers(request):
    data = models.Volunteer.objects.all()
    return render(request, 'Volunteers.html', {'vulData': data})


def volunteerProfile(request, volid):
    data = models.Volunteer.objects.filter(id=volid)
    return render(request, 'Volunteer-Profile.html', {'vulProfile': data})


def gallery(request):
    photos = models.Gallery.objects.all()
    return render(request, 'Gallery.html', {'Photos': photos})


def donation(request):
    return render(request, 'Donation.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name').title()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message').title()
        models.Contact(Name=name, Email=email, Phone=phone, Message=message, Date=todayDate, Time=timeNow).save()
        messages.success(request, "Your Message Has Been Sended Successfully")
    return render(request, 'Contact.html')


def about(request):
    voluntreers = models.Volunteer.objects.all()
    projects = models.Volunteer.objects.all()
    return render(request, 'About.html', {'volunteers': voluntreers, 'projects': projects})


def footerNews(request):
    events = models.Event.objects.all()[:5]
    projects = models.Project.objects.all()[:5]
    return {'events': events, 'projects': projects}
