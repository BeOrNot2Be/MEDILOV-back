from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse

from .models import Photo, Gallery, GalleryTopic, Service, AboutUnit



def ContactView(request):
    return HttpResponse("in development")

def GalleriesView(request):
    return 

def GalleryView(request):

def ServiceView(request):
    services = Service.objects.all()
    return HttpResponse(services)

def AboutView(request):
    units = AboutUnit.objects.order_by('parent')
    return HttpResponse(units)

"""
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
"""