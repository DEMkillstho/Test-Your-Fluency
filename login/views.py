from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')
