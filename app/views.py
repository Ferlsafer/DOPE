from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.models import *
# Create your views here.
def home(request):
    categories = Category.objects.all().order_by('-id')
    return render(request, 'category/index.html', {'categories': categories})

def add_category(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            Category.objects.create(name=name)
            messages.success(request, "Category added successfuly")
            return redirect('home')
    except Exception as e:
        messages.error(request, "Error occured")
        return redirect('home')

def delete_category(request, id):
    try:
        category = get_object_or_404(Category, id=id)
        category.delete()
        messages.success(request, "Category deleted successfuly")
        return redirect('home')
    except Category.DoesNotExist as e:
        print(str(e))
        messages.error(request, "Error occured")
        return redirect('home')

def edit_category(request, id):
    try:
        if request.method == "POST":
            name = request.POST['name']
            category = get_object_or_404(Category, id=id)
            category.name = name
            category.save()
            messages.success(request, "Category updated successfuly")
            return redirect('home')
        category = get_object_or_404(Category, id=id)
        return render(request, 'category/edit.html', {'category': category})
    except Category.DoesNotExist as e:
        print(str(e))
        messages.error(request, str(e.args[0]))
        return redirect('home')