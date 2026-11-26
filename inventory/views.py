from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductForm


def All_Products(request):
    products = Products.objects.all()
    return render(request, "inventory_templates/all_products.html",{"products":products})

def Add_Product(request):
    product_form =ProductForm()
    if request.method == "POST":
        product_form = ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect("allproducts")
    return render(request, "inventory_templates/add_and_edit_product.html", {"product_form": product_form})


def Update_Product(request,pk):
    product = Products.objects.get(id=pk)
    edit_product_form = ProductForm(instance=product)
    if request.method == "POST":
        edit_product_form = ProductForm(request.POST,request.FILES,instance=product)
        if edit_product_form.is_valid():
            edit_product_form.save()
            return redirect("allproducts")
    return render(request,"inventory_templates/add_and_edit_product.html",{"edit_product_form":edit_product_form})

def Delete_Product(request,pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return redirect("allproducts")