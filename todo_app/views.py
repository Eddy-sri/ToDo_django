from django.shortcuts import render
from .models import Todo

# Create your views here.

def home(request):
    todos = Todo.objects.all()
    return render (request, 'home.html', {'tasks':todos})

def detail(requst,id):
    todo = Todo.objects.filter(id = id)
    return render(requst, 'detail.html', {'task':todo})