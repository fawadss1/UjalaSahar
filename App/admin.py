from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Date', 'Time', 'Location')
    list_filter = ('Title', 'Date', 'Location')
    search_fields = ('Title', 'Date', 'Location')


@admin.register(models.Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Date', 'Location')
    list_filter = ('Title', 'Date', 'Location')
    search_fields = ('Title', 'Date', 'Location')


@admin.register(models.Volunteer)
class VolunteersAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Employment', 'Qualification')
    list_filter = ('Name', 'Employment', 'Qualification')
    search_fields = ('Name', 'Employment', 'Qualification')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Date', 'Time')
    list_filter = ('Name', 'Date')
    search_fields = ('Name', 'Email')


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('Image_Title',)
