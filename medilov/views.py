from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Photo, Gallery, GalleryTopic, Service, AboutUnit
from .forms import NameForm
from .email import send_appoitment_registration
import sys


def ContactView(request):
    context = {
        "services": Service.objects.all(),
        "email": None,
        "sent":None
        }
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            email_data = {
                'name':form.cleaned_data['form_name'],
                'phone':form.cleaned_data['form_phone'],
                'dates':f"from {form.cleaned_data['datepicker_start']} to {form.cleaned_data['datepicker_end']}",
                'description':form.cleaned_data['form_orderdescription'],
                'job':form.cleaned_data['form_service'],
                'email':form.cleaned_data['form_email']
            }
            context['email'] = email_data['email']
            if 'test' in sys.argv:
                return render(request, "contact.html", context)
            else:
                if send_appoitment_registration(email_data):
                    context['sent'] = True 
                    return render(request, "contact.html", context)
                else:
                    context['sent'] = False
                    return render(request, "contact.html", context)
        else:
            print("not valid...")#DEVELOPMENT
    return render(request, "contact.html", context)


def EmailView(request):
    return render(request, "email.html", {})

def GalleriesView(request):
    
    context = {
        "gallerytopics": GalleryTopic.objects.all()
        }
    return render(request, "work.html", context)

def GalleryView(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    context = {
        "photos": gallery.photos.all(),
        "videos": gallery.videos.all(),
        "gallery": gallery
        }
    return render(request, "gallery.html", context)

def ServiceView(request):
    context = {
            "services": Service.objects.all()
        }

    if request.user_agent.is_mobile:
        return render(request, "services_mobile.html", context)
    else:
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