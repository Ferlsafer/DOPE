from app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_category', views.add_category, name='add_category')
]