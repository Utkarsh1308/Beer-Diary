from django.contrib.auth.models import User
from django import forms
from .models import Beer

class AddBeerForm(forms.ModelForm):
    CHOICES = (
        ("1", "Bottle"),
        ("2", "Draft"),
    )
    serving_type = forms.ChoiceField(choices=CHOICES)
    rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])

    class Meta:
        model = Beer
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
