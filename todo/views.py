from django.shortcuts import render, redirect, get_object_or_404
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

# Edit item takes in the request and the id of the item to be edited
# It uses a built in get_object_or_404 method to find the item to be edited
# and check it exists safely
# If the request is a post request then the form variable is populated
# with the values from the request
# We use the built in method form.is_valid() to check if
# the form is valid (Django), save it and return
# to the edit item page
# the form variable also needs to have an instance of the item to be edited,
# which we have gotten from the get_object_or_404 method


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)
