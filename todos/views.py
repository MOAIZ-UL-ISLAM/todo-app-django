from django.shortcuts import render,redirect
from .forms import TODOform

from .models import TODO

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOform()
        todos =TODO.objects.filter(user=user)

    return render(request,'todos/todo.html', {'form': form ,'todos': todos})


def add_view(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form= TODOform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo =form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('todos')
        else:
            return render(request, 'todos/todo.html', {'form': form})
        
def edit_view(request, todo_id):
    if request.user.is_authenticated:
        user = request.user
        todo = TODO.objects.get(id=todo_id)

        if request.method == 'GET':
            form = TODOform(instance=todo)
            return render(request, 'todos/edit_todo.html', {'form': form, 'todo': todo})

        elif request.method == 'POST':
            form = TODOform(request.POST, instance=todo)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                return redirect('todos')
            else:
                return render(request, 'todos/edit_todo.html', {'form': form, 'todo': todo})


def delete_view(request, todo_id):
    if request.user.is_authenticated:
        TODO.objects.get(id=todo_id).delete()
        return redirect('todos')
