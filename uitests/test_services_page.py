from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from medilov.models import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from django.urls import reverse
import time
import os

class TestServicesPage(StaticLiveServerTestCase):
    @staticmethod
    def create_service(title="", short_description="", long_description="", img_name="", url=""):
        if title != "": 
            s = Service(title=title, short_description=short_description, long_description=long_description, img_name=img_name, url=url)
            s.save()
            return s
    
    def setUp(self):
        imageUrl = 'https://res.cloudinary.com/avilonproductioncdn/image/upload/v1579047178/Family/Oksana%20and%20Alex/Preview.png'
        
        self.s1 = self.create_service('1', "short desc 1", 'long desc 1', 'img alt', imageUrl)
        self.s2 = self.create_service('2', "short desc 2", 'long desc 2', 'img alt', imageUrl)
        self.s3 = self.create_service('3', "short desc 3", 'long desc 3', 'img alt', imageUrl)
        self.s4 = self.create_service('4', "short desc 4", 'long desc 4', 'img alt', imageUrl)

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
    
    def test_services(self):
        self.broweser.get(self.live_server_url + reverse("services"))
        
        # check total number of about units
        SlideshowElement = self.broweser.find_element_by_class_name('slideshow')
        UIServices = SlideshowElement.find_elements_by_class_name("slide")
        ModalServices = Service.objects.all()
        self.assertEquals(len(UIServices), len(ModalServices))
                
        # check layout
        FirstServiceDescription = UIServices[0].find_element_by_class_name('slide__subtitle')
        self.assertEquals(FirstServiceDescription.get_attribute('innerText'), self.s1.short_description)
        
        self.broweser.quit()

    def test_services_mobile(self):
        
        mobile_emulation = { "deviceName": "iPhone 6" }
        chrome_options = webdriver.ChromeOptions()        
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        if settings.WEBDRIVER_PATH:
            desired_capabilities = DesiredCapabilities.CHROME.copy()
            driver = webdriver.Remote(settings.WEBDRIVER_PATH, desired_capabilities=desired_capabilities, options=chrome_options)
        elif os.path.exists("uitests/chromedriver.exe") and os.name == 'nt':
            driver = webdriver.Chrome("uitests/chromedriver.exe", chrome_options=chrome_options)
        elif os.name == 'posix':
            driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
        else:
            driver = webdriver.Remote("http://testHost", DesiredCapabilities.CHROME, options=chrome_options)
            
        driver.get(self.live_server_url + reverse("services"))

        time.sleep(10)
        
        # check total number of about units
        SlideshowElement = driver.find_element_by_class_name('slideshow')
        UIServices = SlideshowElement.find_elements_by_class_name("slide")
        ModalServices = Service.objects.all()
        self.assertEquals(len(UIServices), len(ModalServices))
                
        # check layout
        FirstServiceDescription = UIServices[0].find_element_by_class_name('slide__title')
        self.assertEquals(FirstServiceDescription.get_attribute('innerText'), self.s1.title)
        
        driver.quit()
        

