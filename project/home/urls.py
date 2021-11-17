from django.urls import path
from home import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path('index', view=views.home1, name='home1')
]