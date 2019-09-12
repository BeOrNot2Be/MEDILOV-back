from django.urls import path
from .views import ContactView, GalleriesView, GalleryView, ServiceView, AboutView, EmailView
from django.conf import settings


urlpatterns = [
    path('contacts/', ContactView, name="contact"),
        
    path('', GalleriesView, name="work"),

    path('gallery/<int:gallery_id>', GalleryView, name="gallery"),

    path('services/', ServiceView, name="services"),
    
    path('about/', AboutView, name="about"),

]

if settings.DEBUG:
    urlpatterns.append(path('email/', EmailView, name="email-template")) 