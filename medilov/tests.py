from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Photo, GalleryTopic, Gallery
from .serializers import PhotoSerializer, GallerySerializer, GalleryTopicSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

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


class GetAllPhotosTest(BaseViewTest):

    def test_get_all_photos(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("photos-all")
        )
        # fetch the data from db
        expected = Photo.objects.all()
        serialized = PhotoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)