from django.urls import path
from rent import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path("/rentbike", view=views.rentBike, name="rentbike"),
    path("/returnbike", view=views.returnBike, name="returnbike"),
    path("/", view=views.logoutPage, name='logout'),
    path("/index", view=views.index, name='index')
]