from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Todo

from .forms import TodoCreateForm , TodoUpdateForm
# Create your views here.

def home(request):
    todos = Todo.objects.all()
    return render (request, 'home.html', {'tasks':todos})

def detail(requst,id):
    todo = Todo.objects.get(id = id)
    return render(requst, 'detail.html', {'task':todo})

def delete(request,id):
    Todo.objects.get(id = id).delete()
    messages.success(request, 'your task deleted successfully', 'success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title = cd['title'], body = cd['body'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form':form})


def update (request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo was update successfully', 'success')
            return redirect('home')
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form':form})
