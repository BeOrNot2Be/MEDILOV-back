from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from medilov.models import AboutUnit
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
import os

class TestAboutPage(StaticLiveServerTestCase):
    @staticmethod
    def create_about_unit(title="", url="", short_description="", phrase="", parent=None ):
        if title != "":
            if parent:
                au = AboutUnit(title=title, url=url, short_description=short_description, phrase=phrase, parent=parent, color="#000000")
            else:
                au = AboutUnit(title=title, url=url, short_description=short_description, phrase=phrase, color="#000000")                
            au.save()
            return au
    
    def setUp(self):
        imageUrl = 'https://res.cloudinary.com/avilonproductioncdn/image/upload/v1579047178/Family/Oksana%20and%20Alex/Preview.png'
        
        self.au1 = self.create_about_unit('1', imageUrl, 'short desc 1', 'phrase 1')
        self.au2 = self.create_about_unit('2', imageUrl, 'short desc 2', 'phrase 2', self.au1)
 
        if os.path.exists("uitests/chromedriver.exe"):
            self.broweser = webdriver.Chrome('uitests/chromedriver.exe')
        else:
            self.broweser = webdriver.Remote("http://testHost", DesiredCapabilities.CHROME)
        time.sleep(5) 
    
    def tearDown(self):
        time.sleep(5) 
        self.broweser.quit()
    
    def test_about_units(self):
        self.broweser.get(self.live_server_url + reverse("about"))
        
        # check total number of about units
        UIAboutUnits = self.broweser.find_elements_by_class_name('content__item')
        ModalAboutUnits = AboutUnit.objects.all()
        self.assertEquals(len(UIAboutUnits), len(ModalAboutUnits))
                
        # check layout
        FirstAboutUnitDescription = self.broweser.find_elements_by_class_name('content__item-description')[0]
        self.assertEquals(FirstAboutUnitDescription.get_attribute('innerText'), self.au1.short_description)

        SecondAboutUnitDescription = self.broweser.find_elements_by_class_name('content__item-description')[1]
        self.assertEquals(SecondAboutUnitDescription.get_attribute('innerText'), self.au2.short_description)