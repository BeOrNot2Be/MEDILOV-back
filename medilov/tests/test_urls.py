from django.test import SimpleTestCase
from django.urls import resolve, reverse
from medilov.views import GalleriesView, GalleryView, ServiceView, AboutView, ContactView, EmailView
from django.conf import settings

class TestUrls(SimpleTestCase):
        
    def test_about_url_is_resolved(self):
        url = reverse("about")
        self.assertEquals(resolve(url).func, AboutView)
    
    def test_work_url_is_resolved(self):
        url = reverse("work")
        self.assertEquals(resolve(url).func, GalleriesView)
    
    def test_gallery_url_is_resolved(self):
        url = reverse("gallery", args=['1'])
        self.assertEquals(resolve(url).func, GalleryView)
    
    def test_contacts_url_is_resolved(self):
        url = reverse("contact")
        self.assertEquals(resolve(url).func, ContactView)
    
    def test_services_url_is_resolved(self):
        url = reverse("services")
        self.assertEquals(resolve(url).func, ServiceView)

    def test_email_url_is_resolved(self):
        if settings.DEBUG:
            url = reverse("email-template")
            self.assertEquals(resolve(url).func, EmailView)
        else:
            pass
