from django.db import models


class Gallery(models.Model):
    Image_Title = models.CharField(max_length=30, blank=True)
    Image_Desc = models.CharField(max_length=255, blank=True)
    Image = models.ImageField(upload_to='Gallery')
