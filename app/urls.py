from app import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_category', views.add_category, name='add_category'),
    path('delete_category/<str:id>', views.delete_category, name="delete_category"),
    path('edit_category/<str:id>', views.edit_category, name="edit_category")
]