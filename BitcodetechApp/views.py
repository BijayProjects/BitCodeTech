from django.shortcuts import render
from .models import Email_Soon
from django.contrib import messages

# Create your views here.

def coming_soon(request):
    if request.method =='POST':
        Email = request.POST['email']
        sv_email = Email_Soon(eMail = Email)
        sv_email.save()
        messages.info(request, 'Your Email is Successfully Sended.')
    return render(request, 'main/soon.html')