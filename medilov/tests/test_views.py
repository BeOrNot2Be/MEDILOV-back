from django.test import TestCase, Client
from django.urls import reverse
from medilov.models import Gallery, GalleryTopic, Video, Photo, Service, AboutUnit
import json

class TestView(TestCase):
    
    @staticmethod
    def create_photo(title="", url="", gallery=None):
        if title != "" and url != "":
            if gallery:
                p = Photo(title=title, url=url, gallery=gallery)
            else:
                p = Photo(title=title, url=url)
            p.save()
            return p

    @staticmethod
    def create_gallery(title="", description="", gallery_logo="", topic=None):
        if title != "":
            if topic:
                g = Gallery(title=title, description=description, gallery_logo=gallery_logo, topic=topic)
            else:
                g = Gallery(title=title, description=description, gallery_logo=gallery_logo)
            g.save()
            return g

    @staticmethod
    def create_gallery_topic(title=""):
        if title != "": 
            gt = GalleryTopic(title=title)
            gt.save()
            return gt
    
    def setUp(self):
        
        gt1 = self.create_gallery_topic('1')
        gt2 = self.create_gallery_topic('2')
        gt3 = self.create_gallery_topic('3')

        g1 = self.create_gallery('1', '1 desc', 'logo', gt1)
        g2 = self.create_gallery('2', '2 desc', 'logo', gt2)
        g3 = self.create_gallery('3', '3 desc', 'logo', gt3)

        p1 = self.create_photo('1', '1 img', g1)
        p2 = self.create_photo('2', '2 img', g2)
        p3 = self.create_photo('3', '3 img', g3)
        
        self.client = Client()
        self.about_url = reverse('about')
        self.work_url = reverse('work')
        self.gallery_url = reverse("gallery", args=[g2.id])
        self.services_url = reverse('services')
        self.contact_url = reverse('contact')
        
        
    def test_about_page_GET(self):        
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        
    def test_work_page_GET(self):        
        response = self.client.get(self.work_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'work.html')
        
    def test_gallery_page_GET(self):
        response = self.client.get(self.gallery_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        
    def test_services_page_GET(self):        
        response = self.client.get(self.services_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')
        
    def test_services_mobile_page_GET(self):        
        
        header = {'HTTP_USER_AGENT': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

        response = self.client.get(self.services_url, data=None, follow=False, secure=False,  **header)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services_mobile.html')
        
    def test_contact_page_GET(self):        
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        
    def test_contact_page_POST(self):        
        response = self.client.post(self.contact_url, {
            "form_name": "Tim",
            "form_email": "xxxxxxxxxx@gmail.com",
            "form_phone": "9999999999",
            "datepicker_start": "03/06/2020",
            "datepicker_end": "03/08/2020",
            "form_service": "wedding photography",
            "form_orderdescription": "test"
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')