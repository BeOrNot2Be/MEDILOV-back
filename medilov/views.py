from rest_framework import generics
from .models import Photo, Gallery, GalleryTopic, Service, AboutUnit
from .serializers import PhotoSerializer, GallerySerializer, GalleriesSerializer, GalleryTopicSerializer, ServiceSerializer, AboutUnitSerializer


class ListPhotosView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class ListGalleryView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class ListGalleriesView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleriesSerializer

class ListGalleryTopicsView(generics.ListAPIView):
    queryset = GalleryTopic.objects.all()
    serializer_class = GalleryTopicSerializer

class ListServicesView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ListAboutUnitView(generics.ListAPIView):
    queryset = AboutUnit.objects.order_by('parent')
    serializer_class =  AboutUnitSerializer
