from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.show, name='show'),
    path('edit', views.edit_profile, name='edit'),
]
