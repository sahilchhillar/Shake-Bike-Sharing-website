from django.urls import path
from bill import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path("/index", view=views.index, name='index')
]