from django import forms
from django.forms import ModelForm
from .models import Doctor 
class DateInput(forms.DateInput):
    input_type='date'

class PasswordField(forms.CharField):
    widget = forms.PasswordInput
class Registerform(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'
        widgets={
            'birthdate':DateInput(),
            'password': forms.PasswordInput()
        }
            
        
