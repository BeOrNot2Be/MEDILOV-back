from django.test import TestCase
from medilov.models import Gallery, GalleryTopic, Video, Photo, Service, AboutUnit

class TestModels(TestCase):
    
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
    def create_video(title="", url="", preview="", gallery=None):
        if title != "" and url != "" and preview != "":
            if gallery:
                v = Video(title=title, url=url, preview=preview, gallery=gallery)
            else:
                v = Video(title=title, url=url, preview=preview)
            v.save()
            return v

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
        
    @staticmethod
    def create_service(title="", short_description="", long_description="", img_name="", url=""):
        if title != "": 
            s = Service(title=title, short_description=short_description, long_description=long_description, img_name=img_name, url=url)
            s.save()
            return s
        
    @staticmethod
    def create_about_unit(title="", url="", short_description="", phrase="", parent="" ):
        if title != "":
            if parent:
                au = AboutUnit(title=title, url=url, short_description=short_description, phrase=phrase, parent=parent, color="#000000")
            else:
                au = AboutUnit(title=title, url=url, short_description=short_description, phrase=phrase, color="#000000")                
            au.save()
            return au
    
    def setUp(self):
        
        self.gt1 = self.create_gallery_topic('1')
        self.gt2 = self.create_gallery_topic('2')
        self.gt3 = self.create_gallery_topic('3')

        self.g1 = self.create_gallery('1', '1 desc', 'logo', self.gt1)
        self.g2 = self.create_gallery('2', '2 desc', 'logo', self.gt2)
        self.g3 = self.create_gallery('3', '3 desc', 'logo', self.gt3)

        self.p1 = self.create_photo('1', '1 img', self.g1)
        self.p2 = self.create_photo('2', '2 img', self.g2)
        self.p3 = self.create_photo('3', '3 img', self.g3)
        
        self.v1 = self.create_video('1', '1 video', '1 img preview', self.g1)
        
        self.s1 = self.create_service('1', "short desc 1", 'long desc 1', 'img alt', 'img url')

        self.au1 = self.create_about_unit('1', 'url 1', 'short desc 1', 'phrase 1')
        self.au2 = self.create_about_unit('2', 'url 2', 'short desc 2', 'phrase 2', self.au1)
        
    def test_galley_topic_instance(self):
        self.assertEquals(self.gt1.title, '1')

    def test_galley_instance_topic_instance_inheritance(self):
        self.assertEquals(self.g2.title, '2')
        self.assertEquals(self.g2.description, '2 desc')
        self.assertEquals(self.g2.gallery_logo, 'logo')
        self.assertEquals(self.g2.topic, self.gt2)
        self.assertIsNotNone(self.g2.date)

    def test_photo_instance_gallery_instance_inheritance(self):
        self.assertEquals(self.p3.title, '3')
        self.assertEquals(self.p3.url, '3 img')
        self.assertIsNotNone(self.p3.date)
        self.assertEquals(self.p3.gallery, self.g3)
        
    def test_gallery_topic_photo_tree(self):
        self.assertEquals(self.p3.gallery.topic, self.gt3)
        
    def test_video_instance_gallery_instance_inheritance(self):
        self.assertEquals(self.v1.title, '1')
        self.assertEquals(self.v1.url, '1 video')
        self.assertEquals(self.v1.preview, '1 img preview')
        self.assertEquals(self.v1.gallery, self.g1)
        
    def test_gallery_topic_video_tree(self):
        self.assertEquals(self.v1.gallery.topic, self.gt1)
        
    def test_service_instance(self):
        self.assertEquals(self.s1.title, '1')
        self.assertEquals(self.s1.short_description, 'short desc 1')
        self.assertEquals(self.s1.long_description, 'long desc 1')
        self.assertEquals(self.s1.img_name, 'img alt')
        self.assertEquals(self.s1.url, 'img url')
        self.assertIsNotNone(self.s1.date)
    
    def test_about_unit_instance(self):
        self.assertEquals(self.au1.title, '1')
        self.assertEquals(self.au1.short_description, 'short desc 1')
        self.assertEquals(self.au1.phrase, 'phrase 1')
        self.assertEquals(self.au1.url, 'url 1')
        self.assertEquals(self.au1.color, '#000000')
    
    def test_about_unit_instance_inheritance(self):
        self.assertEquals(self.au2.parent, self.au1)
    