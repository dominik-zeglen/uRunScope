from django.urls import path
from . import views

app_name = 'trainings'
urlpatterns = [
    path('add/', views.add, name='add'),
    path('show/<int:pk>/', views.show, name='show'),
]
