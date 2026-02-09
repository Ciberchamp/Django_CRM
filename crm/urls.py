from django.urls import path
from .views import dashboard, customer_list, add_customer, delete_customer, edit_customer

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("customers/", customer_list, name="customers"),
    path("customers/add/", add_customer, name="add_customer"),
    path("customers/edit/<int:pk>/", edit_customer, name="edit_customer"),
    path("customers/delete/<int:pk>/", delete_customer, name="delete_customer"),
]
