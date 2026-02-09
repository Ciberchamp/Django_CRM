from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout

@login_required
def dashboard(request):
    return render(request, "crm/dashboard.html")

@login_required
def customer_list(request):
    customers = Customer.objects.filter(user=request.user)
    return render(request, "crm/customer_list.html", {"customers": customers})


@login_required
def add_customer(request):
    if request.method == "POST":
        Customer.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            status=request.POST.get("status"),
            image=request.FILES.get("image"),
            notes=request.POST.get("notes"),
        )
        return redirect("customers")

    return render(request, "crm/add_customer.html")

@login_required
def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk, user=request.user)
    customer.delete()
    return HttpResponse("")

@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk, user=request.user)

    if request.method == "POST":
        customer.name = request.POST.get("name")
        customer.email = request.POST.get("email")
        customer.phone = request.POST.get("phone")
        customer.status = request.POST.get("status")
        if request.FILES.get("image"):
            customer.image = request.FILES.get("image")
        customer.notes = request.POST.get("notes")
        customer.save()
        return redirect("customers")

    return render(request, "crm/edit_customer.html", {"customer": customer})

def logout_view(request):
    logout(request)
    return redirect("login")