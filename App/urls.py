from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.home),
                  path('donations', views.donation, name='donations'),
                  path('gallery', views.gallery, name='gallery'),
                  path('volunteers', views.volunteers, name='volunteers'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
