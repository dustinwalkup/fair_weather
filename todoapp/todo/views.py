from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todo.models import Todo
from django.http import HttpResponseRedirect
from todo.services import get_weather

# Create your views here.

def index_view(request, *args, **kwargs):
    todo_items = Todo.objects.all().order_by("-added_date")
    todo_items = add_data(todo_items)
    return render(request, "index.html", {
        "todo_items": todo_items,
    })

@csrf_exempt
def add_todo_view(request, *args, **kwargs):
    current_date = timezone.now()
    content = request.POST["content"]
    current_zip = request.POST["zip"]
    desired_temp = request.POST["temp"]
    Todo.objects.create(added_date = current_date, text = content, required_temp = desired_temp, zip = current_zip)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo_view(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

def add_data(todo_list):
    completed_zips = []
    current_weather = {}
    for todo in todo_list:
        if todo.zip not in completed_zips:
            api_data = get_weather(todo.zip)
            current_weather[todo.zip] = api_data
            completed_zips.append(todo.zip)
        todo.current_temp = int(current_weather[todo.zip]["temp"])
        todo.city = current_weather[todo.zip]["city"]
    return todo_list