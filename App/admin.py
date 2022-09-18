from django.contrib import admin
from . import models

admin.site.site_header = "Welcome to Ujala Sahar Organization Admin Pannel"
admin.site.site_title = "USO Admin Pannel"
admin.site.index_title = "USO Admin"


admin.site.register(models.Event)
admin.site.register(models.Project)
admin.site.register(models.Volunteer)
admin.site.register(models.Gallery)
admin.site.register(models.Contact)
