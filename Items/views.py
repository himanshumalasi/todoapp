from django.shortcuts import render , redirect
from django.contrib import messages
from .models import TodoList
from .forms import ListItem


# Create your views here.

def home(request):
        if request.method == "POST":
                print()
                form = ListItem(request.POST)
                if form.is_valid():
                        form.save()
                        all_items = TodoList.objects.all
                        messages.success(request,('Item has been added to list!'))
                        return render(request,"Items/todo.html",{'all_items':all_items})
        all_items = TodoList.objects.all
        return render(request,'Items/todo.html',{'all_items':all_items})
        
def delete(request,id):
        item = TodoList.objects.get(pk=id)
        item.delete()
        messages.success(request,('Item has been deleted!'))
        return redirect('home')

def cross_off(request,id):
        item = TodoList.objects.get(pk = id)
        item.completed = True
        item.save()
        return redirect('home')

def uncross(request,id):
        item = TodoList.objects.get(pk = id)
        item.completed = False
        item.save()
        return redirect('home')

def edit(request,id):
        if request.method == 'POST':
                item = TodoList.objects.get(pk=id)
                form = ListItem(request.POST or None, instance = item)
                if form.is_valid():
                        form.save()
                        messages.success(request,("Item has been edited!"))
                        return redirect('home')
        else:
                item = TodoList.objects.get(pk=id)
                return render(request,'Items/edit.html',{'item':item})