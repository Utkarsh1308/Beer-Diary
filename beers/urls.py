from django.urls import path
from . import views

app_name = "beers"

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:beer>', views.beer, name='beer'),
    path('add/beer', views.AddBeer.as_view(), name='add_beer'),
    path('<slug:pk>/update', views.UpdateBeer.as_view(), name='update_beer'),
    path('<slug:pk>/delete', views.DeleteBeer.as_view(), name='delete_beer')
]
