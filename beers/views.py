from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView, DeleteView, View
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

from .models import Beer
from .forms import AddBeerForm, UserForm

# Create your views here.
def index(request):
    Beers = Beer.objects.all()
    context = {
        'Beers': Beers
    }

    return render(request, 'beers/index.html', context)

def detail(request):
    Beers = Beer.objects.all()
    context = {
        'Beers': Beers
    }

    return render(request, 'beers/detail.html', context)

def beer(request, beer):
    def get_beer(beer):
        if '_' in str(beer):
            sections = beer.split('_')
            sections = [section.capitalize() for section in sections]
            y = " ".join(sections)
            return y
        return beer.upper() if len(beer) == 2 else beer.capitalize()

    Beers = Beer.objects.all()
    section = get_object_or_404(Beer, name=get_beer(beer))
    context = {
        'section': section,
        'Beers': Beers,
    }
    return render(request, 'beers/beer.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('beers:index')
    Beers = Beer.objects.all()
    context = {
        "form": form,
        'Beers': Beers,
    }
    return render(request, 'beers/register.html', context)

def login_user(request):
    Beers = Beer.objects.all()
    context = {
        'Beers': Beers,
    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user = User.objects.get(username=username)
                return render(request, 'beers/index.html', {'user': user, 'Beers': Beers})
            else:
                return render(request, 'beers/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'beers/login.html', {'error_message': 'Invalid login'})
    return render(request, 'beers/login.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    Beers = Beer.objects.all()
    context = {
        "form": form,
        'Beers': Beers,
    }
    return render(request, 'beers/index.html', context)

class AddBeer(CreateView):
    form_class = AddBeerForm
    template_name = 'beers/add_beer.html'
    success_url = reverse_lazy('beers:detail')

class UpdateBeer(UpdateView):
    form_class = AddBeerForm
    template_name = 'beers/add_beer.html'
    model = Beer
    success_url = reverse_lazy('beers:detail')

class DeleteBeer(DeleteView):
    model = Beer
    success_url = reverse_lazy('beers:detail')
