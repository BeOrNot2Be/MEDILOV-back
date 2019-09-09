from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Photo, Gallery, GalleryTopic, Service, AboutUnit
from .forms import NameForm
from .email import send_appoitment_registration


def ContactView(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            email_data = {
                'name':form.cleaned_data['form_name'],
                'phonenumber':form.cleaned_data['form_phone'],
                'dates':f"from {form.cleaned_data['datepicker_start']} to {form.cleaned_data['datepicker_end']}",
                'description':form.cleaned_data['form_orderdescription'],
                'job':form.cleaned_data['form_service'],
            }
            send_appoitment_registration(form.cleaned_data['form_email'], email_data)
        else:
            print("not valid...")#DEVELOPMENT
    context = {
        "services": Service.objects.all()
        }
    return render(request, "contact.html", context)

def GalleriesView(request):
    
    context = {
        "gallerytopics": GalleryTopic.objects.all()
        }
    return render(request, "work.html", context)

def GalleryView(request, gallery_id):
    
    context = {
        "gallery": Gallery.objects.get(id=gallery_id)
        }
    return render(request, "gallery.html", context)

def ServiceView(request):

    context = {
        "services": Service.objects.all()
        }
    return render(request, "services.html", context)

def AboutView(request):

    context = {
        "units": AboutUnit.objects.order_by('parent')
        }
    return render(request, "about.html", context)

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