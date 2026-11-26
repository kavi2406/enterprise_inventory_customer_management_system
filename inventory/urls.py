from django.urls import path
from .views import *

urlpatterns = [
    path('allproducts/',All_Products,name="allproducts"),
    path('addproduct/',Add_Product,name="addproduct"),
    path('updateproduct/<int:pk>',Update_Product,name="updateproduct"),
    path('deleteproduct/<int:pk>',Delete_Product,name="deleteproduct"),
]