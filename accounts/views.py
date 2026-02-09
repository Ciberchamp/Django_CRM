from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            login(request, user)
            return redirect("dashboard")
        return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
