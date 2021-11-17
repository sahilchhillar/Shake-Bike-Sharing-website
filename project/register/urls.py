from django.urls import path
from register import views

urlpatterns = [
    path('', view=views.register, name='register'),
    path('/login', view=views.login_user, name='login_user')
]