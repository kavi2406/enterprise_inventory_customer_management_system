from django.urls import path
from .views import *

urlpatterns = [
    path('allcustomers/',All_Customers,name="allcustomers"),
    path('addcustomer/',Add_Customer,name="addcustomer"),
    path('update/<int:id>/',Update_Customer,name="updatecustomer"),
    path('delete/<int:id>/',Delete_Customer,name="deletecustomer")
    
]