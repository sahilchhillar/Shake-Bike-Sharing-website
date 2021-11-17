from django.shortcuts import redirect, render
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def contact(request):
    form = FeedbackForm()
    if form.is_valid():
        form.save()
        return redirect(submit)
    return render(request, template_name='contact/index.html', context={})


def submit(request):
    print(request.POST)
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj = Feedback.objects.create(email=email, message=message)
        obj.save()
    return render(request,template_name='contact/index.html',context={'formSubmit': "Form submitted! Congratulations"})
