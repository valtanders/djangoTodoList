from django.shortcuts import render, redirect
from django.contrib import messages
from .models import List
from .forms import ListForm

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            created_item = form.save()
            messages.success(request, f"Item: <{created_item.item}> has been added to the list!")
    items = List.objects.all
    return render(request, 'home.html', {'items': items})

def about(request):
    my_first_name = "Bruno Antonio"
    my_last_name = "Bollati"
    context = {'first_name': my_first_name,'last_name':my_last_name}
    return render(request, 'about.html', context)

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, f"Item: <{item.item}> has been deleted!")
    return redirect('home')

def update(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = not item.completed
    item.save()
    messages.success(request, f"Item: <{item.item}> has been updated!")
    return redirect('home')

def edit(request, list_id):
    item = List.objects.get(pk=list_id)
    if request.method == 'POST':
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            edited_item = form.save()
            messages.success(request, f"Item: <{edited_item.item}> has been Edited!")
            return redirect('home')
    return render(request, 'edit.html', {'item': item})
    