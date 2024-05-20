from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['password2']

        if password == confirm:
            email_exists = User.objects.filter(email=email).exists()
            username_exists = User.objects.filter(username=username).exists()
            if email_exists:
                messages.info(request, 'Email Already Used')
                return redirect(reverse('registration'))
            elif username_exists:
                messages.info(request,'Username already used')
                return redirect(reverse('registration'))
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords did not match each other')
            return redirect(reverse('registration'))
    else:
        return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('index'))
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect(reverse('login'))
    else:
        return render(request, 'login.html')
def about_us(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def our_protein(request):
    return render(request, 'our_protein.html')