from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  
from django.http import HttpResponse       
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, "restaurant/home.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if password1 != password2:
            return render(request, "restaurant/register.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "restaurant/register.html", {"error": "Username already exists"})

        if email and User.objects.filter(email=email).exists():
            return render(request, "restaurant/register.html", {"error": "Email already exists"})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)  # auto login after register
        return redirect("home")

    return render(request, "restaurant/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request, "restaurant/login.html", {"error": "Invalid username or password"})

    return render(request, "restaurant/login.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("home")

# resturant views 
@login_required
def restaurant_account_view(request):
    return render(request, "restaurant/account.html")

@login_required
def restaurant_meal_view(request):
    return render(request, "restaurant/meal.html")

@login_required
def restaurant_order_view(request):
    return render(request, "restaurant/order.html")

@login_required
def restaurant_report_view(request):
    return render(request, "restaurant/report.html")