from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path
from operator_data import views

urlpatterns = [
    path('', view=views.home, name='operator_login'),
    path('drop', view=views.drop_bike, name='drop'),
    path('display', view=views.display, name='display')
]