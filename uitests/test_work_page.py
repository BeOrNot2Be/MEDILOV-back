from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from medilov.models import Gallery, GalleryTopic
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.conf import settings
import time
import os

class TestWorkPage(StaticLiveServerTestCase):
    @staticmethod
    def create_gallery_topic(title=""):
        if title != "": 
            gt = GalleryTopic(title=title)
            gt.save()
            return gt
        
    @staticmethod
    def create_gallery(title="", description="", gallery_logo="", topic=None):
        if title != "":
            if topic:
                g = Gallery(title=title, description=description, gallery_logo=gallery_logo, topic=topic)
            else:
                g = Gallery(title=title, description=description, gallery_logo=gallery_logo)
            g.save()
            return g
    
    def setUp(self):
        imageUrl = 'https://res.cloudinary.com/avilonproductioncdn/image/upload/v1579047178/Family/Oksana%20and%20Alex/Preview.png'
        
        self.gt1 = self.create_gallery_topic('1')
        self.gt2 = self.create_gallery_topic('2')
        self.gt3 = self.create_gallery_topic('3')
        self.gt4 = self.create_gallery_topic('4')
        
        
        self.g1 = self.create_gallery('1', '1 desc', imageUrl, self.gt1)
        self.g2 = self.create_gallery('2', '2 desc', imageUrl, self.gt2)
        self.g22 = self.create_gallery('2.2', '2.2 desc', imageUrl, self.gt2)
        self.g3 = self.create_gallery('3', '3 desc', imageUrl, self.gt3)
        
        if settings.WEBDRIVER_PATH:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--remote-debugin-port=9222")
            options.add_argument("--screen-size=1200x800")
            self.broweser = webdriver.Remote(settings.WEBDRIVER_PATH, desired_capabilities=options.to_capabilities())
        elif os.path.exists("uitests/chromedriver.exe") and os.name == 'nt':
            self.broweser = webdriver.Chrome("uitests/chromedriver.exe")
        elif os.name == 'posix':
            self.broweser = webdriver.Chrome('chromedriver')
        else:
            self.broweser = webdriver.Remote("http://testHost", desired_capabilities=DesiredCapabilities.CHROME)

        time.sleep(5) 

    def tearDown(self):
        time.sleep(5) 
        self.broweser.quit()
    
    def test_gallery_topics_and_galleries(self):
        self.broweser.get(self.live_server_url)        
        
        # check total number of gallery topics
        UIStacks = self.broweser.find_elements_by_class_name('stack')
        ModalStacks = GalleryTopic.objects.all()
        self.assertEquals(len(UIStacks), len(ModalStacks))
                
        # check right topic layour
        UIStackSelected = self.broweser.find_element_by_class_name('is-selected')
        self.assertEquals(UIStacks[0], UIStackSelected)

        SelectedStackName = UIStackSelected.find_element_by_class_name('stack-title').find_element_by_tag_name('span')
        self.assertEquals(SelectedStackName.get_attribute('innerText'), self.gt1.title)
        
        # check total number of galleries
        Galleries = self.broweser.find_elements_by_class_name('item')
        ModalGalleries = Gallery.objects.all()
        self.assertEquals(len(Galleries), len(ModalGalleries))
        
        # check right gallery layour
        UINextGalleries = UIStacks[1].find_elements_by_class_name('item')        
        ModalNextGalleries = Gallery.objects.filter(topic=self.gt2)
        
        for ui, m in zip(UINextGalleries, ModalNextGalleries):
            self.assertEquals(ui.find_element_by_tag_name("li").get_attribute('innerText'), m.description)
                        