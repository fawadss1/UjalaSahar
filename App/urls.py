from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.home),
                  path('donation', views.donation, name='donation'),
                  path('about us', views.donation, name='about us'),
                  path('gallery', views.gallery, name='gallery'),
                  path('volunteers', views.volunteers, name='volunteers'),
                  path('volunteer/profile/<int:id>', views.volunteer_profile, name='volunteer profile'),
                  path('projects', views.projects, name='projects'),
                  path('project/details/<int:id>', views.project_detail, name='project details'),
                  path('contact us', views.contact, name='contact'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
