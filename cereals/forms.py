from django import forms
from django.forms import ModelForm
from cereals.models import logg
class authform(forms.ModelForm):
    class Meta:
        model=logg
        fields=['user','passer']
