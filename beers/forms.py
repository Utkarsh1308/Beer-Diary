from django.contrib.auth.models import User
from django import forms
from .models import Beer

class AddBeerForm(forms.ModelForm):
    CHOICES = (
        ("Bottle", "Bottle"),
        ("Draft", "Draft"),
    )
    serving_type = forms.ChoiceField(choices=CHOICES)
    rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])

    class Meta:
        model = Beer
        fields = '__all__'
        exclude = ['author']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
