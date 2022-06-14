from django.shortcuts import render
from django.shortcuts import render
from app.models import Contact
from datetime import datetime

# from django.contrib import messages

# Create your views here.
def index(request):
        # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactme = Contact(name = name, email=email, subject=subject,message=message, date = datetime.today())# creating object of contact
        contactme.save()
        # messages.success(request, 'Your response has been sent!.')
    return render(request, 'index.html')