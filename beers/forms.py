from django import forms
from .models import Beer

class AddBeerForm(forms.ModelForm):

    class Meta:
        model = Beer
        fields = '__all__'
