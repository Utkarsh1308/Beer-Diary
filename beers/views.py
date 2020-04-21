from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Beer

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
