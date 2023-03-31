from django.shortcuts import render
from django.contrib import messages
from . import models


def home(request):
    gallery = models.Gallery.objects.all()
    voluntreers = models.Volunteer.objects.all()
    projects = models.Volunteer.objects.all()
    return render(request, 'Home.html', {'gallery': gallery, 'volunteers': voluntreers, 'projects': projects})


def events(request):
    data = models.Event.objects.all()
    return render(request, 'Events.html', {'EventData': data})


def eventDetails(request, pk, title):
    data = models.Event.objects.get(id=pk)
    return render(request, 'Event-Details.html', {'EventData': data})


def projects(request):
    data = models.Project.objects.all()
    return render(request, 'Projects.html', {'proData': data})


def projectDetails(request, pk, title):
    data = models.Project.objects.get(id=pk)
    return render(request, 'Project-Details.html', {'proDetails': data})


def volunteers(request):
    data = models.Volunteer.objects.all()
    return render(request, 'Volunteers.html', {'vulData': data})


def volunteerProfile(request, pk, name):
    data = models.Volunteer.objects.get(id=pk)
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
        models.Contact(Name=name, Email=email, Phone=phone, Message=message).save()
        messages.success(request, "Your Message Has Been Sended Successfully")
    return render(request, 'Contact.html')


def about(request):
    voluntreers = models.Volunteer.objects.all()
    projects = models.Volunteer.objects.all()
    return render(request, 'About.html', {'volunteers': voluntreers, 'projects': projects})


def education(request):
    voluntreers = models.Volunteer.objects.all()
    projects = models.Volunteer.objects.all()
    return render(request, 'Education.html', {'volunteers': voluntreers, 'projects': projects})


def food(request):
    voluntreers = models.Volunteer.objects.all()
    projects = models.Volunteer.objects.all()
    return render(request, 'Food.html', {'volunteers': voluntreers, 'projects': projects})


def homeless(request):
    voluntreers = models.Volunteer.objects.all()
    projects = models.Volunteer.objects.all()
    return render(request, 'Homeless.html', {'volunteers': voluntreers, 'projects': projects})


def footerNews(request):
    events = models.Event.objects.all()[:5]
    projects = models.Project.objects.all()[:5]
    return {'eventsData': events, 'projectsData': projects}
