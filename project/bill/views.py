from django.shortcuts import render
from rent.models import RentTable

# Create your views here.
def home(request):
    objects = RentTable.objects.filter(userId=request.user)
    obj = objects[len(objects)-1]
    charge = obj.charges
    rentLoc = obj.rentLocation
    returnLoc = obj.returnLocation
    return render(request, template_name='bill/bill.html', context={'charge': charge, 'rent': rentLoc, 'return': returnLoc})


def index(request):
    return redirect('/index')