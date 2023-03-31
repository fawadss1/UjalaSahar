from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Events', views.events, name='events'),
    path('Event/Detail/<slug:title>^<int:pk>', views.eventDetails, name='event details'),
    path('Projects', views.projects, name='projects'),
    path('Project/Detail/<slug:title>^<int:pk>', views.projectDetails, name='project details'),
    path('Volunteers', views.volunteers, name='volunteers'),
    path('Volunteer/Profile/<slug:name>^<int:pk>', views.volunteerProfile, name='volunteer profile'),
    path('Gallery', views.gallery, name='gallery'),
    path('Donation', views.donation, name='donation'),
    path('Contact-us', views.contact, name='contact'),
    path('About-us', views.about, name='about'),
    path('Mession/Education-For-All', views.education, name='educaion'),
    path('Mession/Feed-For-Hungry-Child', views.food, name='food'),
    path('Mession/Home-For-Homeless', views.homeless, name='homeless'),
    re_path(r'^Media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^Static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
