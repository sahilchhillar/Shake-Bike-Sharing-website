from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import ReportBikes
from rent.models import RentTable

def home(request):   
    if request.method == 'POST':
        bikeId = request.POST['bikeId']
        message = request.POST['message']
        report_loc = request.POST['rentloc']
        status = False

        object = ReportBikes(bikeId=bikeId, message=message, status=status, pickup=report_loc)
        object.save()

        return HttpResponseRedirect('/index')

        # object = RentTable.objects.filter(bikeId=bikeId)

        # if object is not None:
        #     object = ReportBikes(bikeId=bikeId, message=message, status=False)
        #     object.save()

        #     redirect('/')
        #     return render(request, template_name='report/index.html', context={'bikeId': 'Bike Id not found'})

        # else:
        #     return render(request, template_name='report/index.html', context={'bikeId': 'Bike Id not found'})

    return render(request, template_name='report/index.html', context={})