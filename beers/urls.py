from django.urls import path
from . import views

app_name = "beers"

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:beer>', views.beer, name='beer'),
    path('add/beer', views.AddBeer.as_view(), name='add_beer')
]
