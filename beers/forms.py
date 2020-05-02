from django.contrib.auth.models import User
from django import forms
from .models import Beer

class AddBeerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(AddBeerForm, self).__init__(*args, **kwargs)

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

    def clean_name(self):
        name = self.cleaned_data.get('name')

        try:
            match = Beer.objects.get(name=name, author=self.user)
        except Beer.DoesNotExist:
            return name

        raise forms.ValidationError('This name already exists. Please choose a different name.')

class UpdateBeerForm(forms.ModelForm):
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
