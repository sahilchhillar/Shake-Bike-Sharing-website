from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from register.models import Balance
from rent.models import RentTable

# Create your views here.
def home(request):
    if request.method == 'POST':
        top_up = round(float(request.POST['count']), 2)
        print(request.user)
        print(top_up)
        balance = Balance.objects.filter(username=request.user)
        print(balance[0].amount)
        balance_amount = round(float(balance[0].amount), 2)
        total = round(balance_amount+top_up, 2)
        print(total)
        balance.update(amount=total)
        return HttpResponseRedirect('wallet')
    return render(request, template_name='wallet/recharge.html', context={})


def homePage(request):
    balance = Balance.objects.filter(username=request.user)
    amount = balance[0].amount
    # objects = RentTable.objects.filter(userId=request.user)
    # if len(objects) == 0:
    #     redirect('/')
    # obj = objects[len(objects)-1]
    # charge = float(obj.charges)
    # amount = float(balance[0].amount) - charge

    # balance.update(amount=round(amount, 2))

    return render(request, template_name='wallet/recharge.html', context={'balance': amount})

    
def index(request):
    return redirect('/index')