from django.test import SimpleTestCase
from medilov.forms import NameForm


class TestForms(SimpleTestCase):
    
    def test_name_form_validation_with_valid_data(self):
        form = NameForm(data={
            "form_name": "Tim",
            "form_email": "xxxxxxxxxx@gmail.com",
            "form_phone": "9999999999",
            "datepicker_start": "03/06/2020",
            "datepicker_end": "03/08/2020",
            "form_service": "wedding photography",
            "form_orderdescription": "test"
        })
        self.assertTrue(form.is_valid())
        
    def test_name_form_validation_without_valid_data(self):
        form = NameForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)