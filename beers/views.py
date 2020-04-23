from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .models import Beer
from .forms import AddBeerForm

# Create your views here.
def index(request):
    Beers = Beer.objects.all()
    context = {
        'Beers': Beers
    }

    return render(request, 'beers/index.html', context)

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

class AddBeer(CreateView):
    form_class = AddBeerForm
    template_name = 'beers/add_beer.html'
    success_url = reverse_lazy('beers:add_beer')
