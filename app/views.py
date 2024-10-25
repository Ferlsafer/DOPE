from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

from app.models import *

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return redirect('user_signup')


def user_logout(request):
    logout(request)
    return redirect('user_signup')

# Create your views here.
@login_required(login_url='user_signup')
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


def user_signup(request):

    cats = Category.objects.all()
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        phone = request.POST['phone']
        address = request.POST['address']
        user = User.objects.create_user(
            username=username,
            password = password,
            email=email
        )
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        Profile.objects.create(
            user=user,
            phone=phone,
            address=address
        )

        return redirect('home')

    return render(request, 'user/register.html', {'cats': cats})


def demo_save(request):
    if request.method == 'POST':
        cat = request.POST['cat']
        print('Category: ', cat)
        if cat == '':
                messages.warning(request, "error")
                return redirect('user_signup')
        try:
            
            category = Category.objects.get(id=cat)
            Demo.objects.create(
                category=category
            )
            messages.success(request, "Demo saved")
            return redirect('user_signup')
        except Category.DoesNotExist as e:
            messages.error(request, str(e))
            return redirect('user_signup')