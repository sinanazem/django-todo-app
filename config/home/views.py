from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Todo
from django.contrib import messages
from home.forms import TodoCreateForm, TodoUpdateForm

# Create your views here.


def introduction(request):
    return render(request, "index.html", {"name": "matin", "position": "ML Engineering", "age": 23})

def todo(request):
    all_todo = Todo.objects.all()
    return render(request, "todo.html", {"todo": all_todo})

def detail(request, todo_id):
    todo_item = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {"todo_item": todo_item})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, "Todo is Deleted Successfully", extra_tags="warning")
    return redirect("todo")

def create(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(
                title=cd["title"],
                description=cd["description"],
                date=cd["date"],
                completed=cd["completed"]
            )
            messages.success(request, "Todo is Created Successfully", extra_tags="success")

            return redirect("todo")
    else:
        form = TodoCreateForm()
    return render(request, "create.html", {"form": form})

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo is Updated Successfully", extra_tags="success")

            return redirect("details", todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, "update.html", {"form": form})























