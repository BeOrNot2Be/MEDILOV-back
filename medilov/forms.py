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