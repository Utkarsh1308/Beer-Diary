from django.urls import path
from . import views

app_name = "beers"

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:beer>', views.beer, name='beer')
]
