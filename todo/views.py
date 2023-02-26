from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.

# This is what returns the HTML template based on the request
# items is getting the Item model and returning everything within it
# context is what allows us to access the data from the Items Model#
# ...its the connection between the models and frontend


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

# If the request type is a post request then get the values from
# the form submitted and set them to the appropriate variables
# This is where we create a new item and save it to the database
# then return to the add item page


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    # Here we pull in the form, with all its field definitions and attributes
    # The context then provides access to the frontend
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

