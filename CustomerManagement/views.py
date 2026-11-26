from django.shortcuts import render,redirect
from .models import Customers
from .forms import CustomerForm


def All_Customers(request):
    customers = Customers.objects.all()
    return render(request,'customer_templates/all_customers.html',{'customers':customers})



def Add_Customer(request):
    customer_form = CustomerForm()

    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('allcustomers')

    return render(request,'customer_templates/add_and_edit_customer.html',{'customer_form':customer_form})



def Update_Customer(request,id):
    customer = Customers.objects.get(id=id)
    edit_customer_form = CustomerForm(instance=customer)

    if request.method == "POST":
        edit_customer_form = CustomerForm(request.POST,instance=customer)
        if edit_customer_form.is_valid():
            edit_customer_form.save()
            return redirect('allcustomers')
        
    return render(request,'customer_templates/add_and_edit_customer.html',{'edit_customer_form':edit_customer_form})



def Delete_Customer(request,id):
    customer = Customers.objects.get(id=id)
    customer.delete()
    return redirect('allcustomers')