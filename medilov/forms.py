from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import AboutUnit

class AboutUnitForm(ModelForm):
    class Meta:
        model = AboutUnit
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }

class NameForm(forms.Form):
    form_name = forms.CharField(label='Name', max_length=100)
    form_email = forms.CharField(label='Email address', max_length=100)
    form_phone = forms.CharField(label='Phone number', max_length=100)
    datepicker_start = forms.CharField(label='From', max_length=100)
    datepicker_end = forms.CharField(label='To', max_length=100)
    form_service = forms.CharField(label='Service', max_length=100)
    form_orderdescription = forms.CharField(label='Order descrition', max_length=1000)