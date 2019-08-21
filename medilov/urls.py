from django.urls import path
from .views import ListPhotosView, ListGalleriesView, ListGalleryTopicsView, ServicesView, AboutUnitView

urlpatterns = [
    path('gallery-topics/', ListGalleryTopicsView.as_view(), name="gallery-topics-all"),
    
    path('photos/', ListPhotosView.as_view(), name="photos-all"),
    
    path('galleries/', ListGalleriesView.as_view(), name="galleries-all"),

    path('services/', ServicesView.as_view(), name="services-all"),
    
    path('about-units/', AboutUnitView.as_view(), name="about-view-all"),

]