from django.shortcuts import render , redirect

from .forms import UserRegistrationForm

from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'],cd['password'])
            messages.success(request, 'user registered successfully', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form':form})