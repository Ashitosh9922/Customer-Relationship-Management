from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashBoard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),

-
    path('create_order/', views.createOrder, name="create_order"),
   
    
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),


    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('create_customer/', views.createCustomer, name="create_customer"),  # New URL for creating a customer

    path('customer/update/<int:pk>/', views.updateCustomer, name='update_customer'),  # Update customer URL
    path('customer/delete/<int:pk>/', views.deleteCustomer, name='delete_customer'),  # Delete customer URL
    path('customer/<int:pk>/', views.customer, name='customer_detail'), 


]
