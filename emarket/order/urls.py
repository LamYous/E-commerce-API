from django.urls import path
from . import views

urlpatterns = [
    path('orders/new', views.new_order, name="new_order"),
    path('orders/', views.all_orders, name="all_orders"),
    path('orders/<str:pk>/', views.get_order, name="get_order"),
    path('orders/process/<str:pk>/', views.process_order, name='process_order'),
    path('orders/delete/<str:pk>/', views.delete_order, name='delete_order'),
]