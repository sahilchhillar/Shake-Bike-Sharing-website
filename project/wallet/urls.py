from django.urls import path
from wallet import views

urlpatterns = [
    path('', view=views.homePage, name='wallet'),
    path('top_up', view=views.home, name='top_up'),
    path("/index", view=views.index, name='index')
]