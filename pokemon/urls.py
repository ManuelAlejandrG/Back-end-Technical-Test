from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'), # home url 
    path('evolution/<name>/', views.EvolutionChange.as_view(), name='evolution'), #evolution url,
    path('info/<id>/', views.PokemonInfo.as_view(), name='info') # info url
]