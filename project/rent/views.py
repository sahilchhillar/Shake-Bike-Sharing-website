import datetime
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout
# from django.core.mail import send_mail
from .models import RentTable
import time
from datetime import date, datetime
from register.models import Balance


# bikeId = random.randint(1,11)

# Create your views here.
def home(request):
    print(request.user)
    return render(
        request, 
        template_name='rent/rent.html',
        context={}
    )

def rentBike(request):
    if request.method == 'POST':
        print(request.user)
        # print(request.POST['rentloc'])
        # print(request.POST['returnloc'])

        # send_mail(
        #     'Bike Id',
        #     f'Your bike id is {bikeId}',
        #     'vsnegi2207@gmail.com',
        #     ['sahil13799@gmail.com'],
        #     fail_silently=False,
        # )
        
        # print(bikeId)
        rentLoc = request.POST['rentloc']
        bikeId = request.POST['bikeId']
        rentDate = date.today()
        t = time.localtime()
        start = time.strftime("%H:%M:%S", t)

        object = RentTable(userId=request.user, bikeId=bikeId, date=rentDate, startTime=start, rentLocation=rentLoc)
        # print(object)
        object.save()

        return render(request,
            template_name='rent/return.html',
            context={'bikeId': bikeId}
        )
    # rentDate = date.today()
    # t = time.localtime()
    # start = time.strftime("%H:%M:%S", t)
    # end = None

    # data = RentTable(date=rentDate, startTime=start, endTime=end)
    # print(data)
    # data.save()

    return render(request,
        template_name='rent/rent.html',
        context={}
    )

def returnBike(request):
    # print(bikeId)
    # print(request.POST['returnloc'])
    print(request.user)
    returnLoc = request.POST['returnloc']
    
    objects = RentTable.objects.filter(userId=request.user, endTime=None)
    t = time.localtime()
    end = datetime.strptime(time.strftime("%H:%M:%S", t), "%H:%M:%S").time()
    start = objects[0].startTime
    print(type(end), end)
    print(type(start), start)

    diff = datetime.combine(date.today(), end) - datetime.combine(date.today(), start)
    print(diff.total_seconds())

    objects.update(endTime=end, returnLocation=returnLoc, charges=round(diff.total_seconds()/60*0.05, 2))

    balance = Balance.objects.filter(username=request.user)
    amount = balance[0].amount
    charge = round(diff.total_seconds()/60*0.05, 2)
    amount -= charge
    balance.update(amount=amount)

    

    # for obj in objects:
    #     if obj.endTime == None:
    #         t = time.localtime()
    #         end = time.strftime("%H:%M:%S", t)
    #         obj.update(endTime=end, returnLocation=returnLoc)
    #         break
    return redirect('/bill')
    

    # objects = RentTable.objects.filter(bikeId=bikeId)

    # if objects is not None:
    #     returnLoc = request.POST['returnloc']
    #     t = time.localtime()
    #     end = time.strftime("%H:%M:%S", t)
    #     objects.update(endTime=end, returnLocation=returnLoc)
    #     # # objects = objects(endTime=end, returnLocation=returnLoc)
    #     # objects.endTime = end
    #     # objects.save()
    #     # objects.returnLocation = returnLoc
    #     # objects.save()

        # return redirect('/')

    # t = time.localtime()
    # end = time.strftime("%H:%M:%S", t)

    # return render(request,
    #     template_name='rent/return.html',
    #     context={}
    # )


def logoutPage(request):
    print(request.user)
    logout(request)
    return HttpResponseRedirect('/')



def index(request):
    return redirect('/index')