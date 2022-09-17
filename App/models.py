from django.db import models


class Gallery(models.Model):
    Image_Title = models.CharField(max_length=30, blank=True)
    Image_Desc = models.CharField(max_length=255, blank=True)
    Image = models.ImageField(upload_to='Gallery')

    def __str__(self):
        return str(self.Image_Title)

    class Meta:
        verbose_name_plural = 'Gallery'


class Volunteer(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Income_Source = models.CharField(max_length=50, blank=True)
    Qualification = models.CharField(max_length=50, blank=True)
    Years_of_Experience = models.IntegerField(blank=True)
    Photo = models.ImageField(upload_to='Volunteers')
    Facebook_Username = models.CharField(max_length=255, blank=True)
    Twitter_Username = models.CharField(max_length=255, blank=True)
    Linkedin_Username = models.CharField(max_length=255, blank=True)
    Describtion = models.TextField(blank=True)

    def __str__(self):
        return str(self.Name)


class Project(models.Model):
    Title = models.CharField(max_length=50, blank=False)
    Date = models.DateField(blank=False, auto_now=False)
    Time = models.TimeField(auto_now=True)
    Location = models.CharField(max_length=255, blank=False)
    Photo = models.ImageField(upload_to='Projects')
    Description = models.TextField(blank=False)

    def __str__(self):
        return str(self.Title)
