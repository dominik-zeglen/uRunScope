from django.urls import path
from . import views

app_name = 'trainings'
urlpatterns = [
    path('add/', views.add, name='add'),
    path('list/', views.show_all, name='list'),
    path('show/<int:pk>/', views.show, name='show'),
]
