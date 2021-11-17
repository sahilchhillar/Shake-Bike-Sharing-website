from django.urls import path
from contact import views

urlpatterns = [
    path('', view=views.contact, name='contact'),
    path('submit', view=views.submit, name='submit')
]