from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('events', views.events, name='events'),
                  path('event/details/<int:evnid>', views.eventDetails, name='event details'),
                  path('projects', views.projects, name='projects'),
                  path('project/details/<int:proid>', views.projectDetails, name='project details'),
                  path('volunteers', views.volunteers, name='volunteers'),
                  path('volunteer/profile/<int:volid>', views.volunteerProfile, name='volunteer profile'),
                  path('gallery', views.gallery, name='gallery'),
                  path('donation', views.donation, name='donation'),
                  path('contact-us', views.contact, name='contact'),
                  path('about-us', views.about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
