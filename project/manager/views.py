from django.shortcuts import render

# Create your views here.
def manager(request):
    return render(request, template_name='manager/manager.html', context={})