from django.urls import path
from .views import ListPhotosView, ListGalleriesView, ListGalleryView, ListGalleryTopicsView, ListServicesView, ListAboutUnitView

urlpatterns = [
    path('gallery-topics/', ListGalleryTopicsView.as_view(), name="gallery-topics-all"),
    
    path('photos/', ListPhotosView.as_view(), name="photos-all"),
    
    path('galleries/', ListGalleriesView.as_view(), name="galleries-all"),

    path('gallery/', ListGalleryView.as_view(), name="gallery-all"),

    path('services/', ListServicesView.as_view(), name="services-all"),
    
    path('about-units/', ListAboutUnitView.as_view(), name="about-view-all"),

]