from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import ToDoList

# Create your views here.
def index(request):
	tdlists = ToDoList.objects.all()
	return render(request, 'todolist/index.html', {'tdlists': tdlists})

def display_list(request, list_id):
	tdlist = get_object_or_404(ToDoList, pk=list_id)
	return render(request, 'todolist/list.html', {'tdlist': tdlist})