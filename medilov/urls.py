from django.urls import path
from .views import ContactView, GalleriesView, GalleryView, ServiceView, AboutView

urlpatterns = [
    path('contacts/', ContactView, name="contact"),
        
    path('', GalleriesView, name="work"),

    path('gallery/<int:gallery_id>', GalleryView, name="gallery"),

    path('services/', ServiceView, name="services"),
    
    path('about/', AboutView, name="about"),

]