from django.db import models


class Event(models.Model):
    Title = models.CharField(max_length=50, blank=False, unique=True)
    Date = models.DateField(blank=False, auto_now=False)
    Time = models.TimeField(auto_now=True)
    Location = models.CharField(max_length=255, blank=False)
    Photo1 = models.ImageField(upload_to='Events', blank=True)
    Photo2 = models.ImageField(upload_to='Events', blank=True)
    Photo3 = models.ImageField(upload_to='Events', blank=True)
    Photo4 = models.ImageField(upload_to='Events', blank=True)
    Photo5 = models.ImageField(upload_to='Events', blank=True)
    Description = models.TextField(blank=False)

    def __str__(self):
        return self.Title


class Project(models.Model):
    Title = models.CharField(max_length=50, blank=False)
    Date = models.DateField(blank=False, auto_now=False)
    Location = models.CharField(max_length=255, blank=False)
    Photo = models.ImageField(upload_to='Projects')
    Description = models.TextField(blank=False)

    def __str__(self):
        return self.Title


Employments = (
    ('Business Man', 'Business Man'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Govt Employee', 'Govt Emp'),
    ('Self Employed', 'Self Employed'),
)


class Volunteer(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Employment = models.CharField(max_length=20, choices=Employments, blank=False)
    Qualification = models.CharField(max_length=50, blank=True)
    Hobbies = models.CharField(max_length=255, blank=False)
    Years_of_Experience = models.IntegerField(blank=False)
    Photo = models.ImageField(upload_to='Volunteers')
    Facebook_Username = models.CharField(max_length=255, blank=True)
    Twitter_Username = models.CharField(max_length=255, blank=True)
    Linkedin_Username = models.CharField(max_length=255, blank=True)
    Describtion = models.TextField(blank=True)

    def __str__(self):
        return self.Name


class Gallery(models.Model):
    Image_Title = models.CharField(max_length=30, blank=True)
    Image = models.ImageField(upload_to='Gallery')

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.Image_Title



class Contact(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Email = models.EmailField(blank=False)
    Phone = models.CharField(max_length=15, blank=False)
    Message = models.TextField(max_length=255)
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.Name
