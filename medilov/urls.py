from django.urls import path
from .views import ContactView, GalleriesView, GalleryView, ServiceView, AboutView

urlpatterns = [
    path('Contacts/', ContactView, name="contact"),
        
    path('work/', GalleriesView, name="work"),

    path('gallery/', GalleryView, name="gallery"),

    path('services/', ServiceView, name="services"),
    
    path('about/', AboutView, name="about"),

]