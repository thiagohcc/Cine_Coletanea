from django.urls import path
from . import views


urlpatterns = [
    path('minha_coletanea/', views.minha_coletanea, name='minha_coletanea'),
    path('item/<str:id>', views.item, name='item'),
]