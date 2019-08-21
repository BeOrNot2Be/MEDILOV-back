from rest_framework import generics
from .models import Photo, Gallery, GalleryTopic, Service, AboutUnit
from .serializers import PhotoSerializer, GallerySerializer, GalleryTopicSerializer, ServiceSerializer, AboutUnitSerializer


class ListPhotosView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class ListGalleriesView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class ListGalleryTopicsView(generics.ListAPIView):
    queryset = GalleryTopic.objects.all()
    serializer_class = GalleryTopicSerializer

class ServicesView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AboutUnitView(generics.ListAPIView):
    queryset = AboutUnit.objects.order_by('parent')
    serializer_class =  AboutUnitSerializer
