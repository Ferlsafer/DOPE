from django.shortcuts import render, redirect
from app.models import *
# Create your views here.
def home(request):
    categories = Category.objects.all().order_by('-id')
    return render(request, 'home.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return redirect('home')