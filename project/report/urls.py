from django.urls import path
from report import views

urlpatterns = [
    path('', view=views.home, name='report'),
]