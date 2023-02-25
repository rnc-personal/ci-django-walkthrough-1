from django.shortcuts import render, redirect
from .models import Item
# Create your views here.

# This is what returns the HTML template based o nthe request
# items is getting the Item model and returning everything within it
# context is what allows us to access the data from the Items Model#
# ...its the connection between the models and frontend


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        # If the request type is a post request then get the values from 
        # the form submitted and set them to the appropriate variables
        name = request.POST.get('name')
        done = 'done' in request.POST
        # This is where we create a new item and save it to the database
        Item.objects.create(name=name, done=done)

        # We send people back to the add item page
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')

