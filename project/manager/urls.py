from django.urls import path
from manager import views

urlpatterns = [
    path('', view=views.manager, name='manager')
]