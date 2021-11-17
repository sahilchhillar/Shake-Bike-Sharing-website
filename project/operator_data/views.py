from django.shortcuts import redirect, render
from report.models import ReportBikes
from .models import Operator_details

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        object = Operator_details.objects.filter(username=username, password=password)
        if len(object) == 0:
            return render(request, template_name='operator_data/login2.html', context={'confirm': 'Invalid credentials'})
        else:
            return redirect('/operatordisplay')
    return render(request, template_name='operator_data/login2.html', context={})

def display(request):
    objects = ReportBikes.objects.all()
    return render(request, template_name='operator_data/table.html', context={'objects': objects})

def drop_bike(request):
    if request.method == 'POST':
        bike = request.POST.get('bike_id')
        loc = request.POST.get('droploc')

        objects = ReportBikes.objects.filter(bikeId=bike, status=False)
        if len(objects) != 0:
            objects.update(status=True, drop=loc)
            # return redirect('/operatordisplay')

        return redirect('/operatordrop')
        # return redirect('/operatordisplay')

    else:
        return render(request, template_name='operator_data/index.html', context={})