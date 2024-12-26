from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_items, name='list_items'),
    path('create/', views.create_item, name='create_item'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path("category/<int:cat_id>", views.get_item_per_category, name='get_item_per_category'),
]