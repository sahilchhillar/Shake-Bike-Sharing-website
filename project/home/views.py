from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user is not None:
        print(request.user)
    else:
        print("No user logged in")
    return render(request, template_name='home/home.html', context={})


def home1(request):
    return render(request, template_name='home/home1.html', context={})