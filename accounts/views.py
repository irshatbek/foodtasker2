from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.template.loader import get_template


@login_required
def home(request):
    return render(request, "home.html")


@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()          # creates the user
        login(request, user)        # auto-login after register
        return redirect("home")

    return render(request, "accounts/register.html", {"form": form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    error = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next")
            return redirect(next_url or "home")
        else:
            error = "Invalid username or password"

    return render(request, "home.html", {"error": error})


@require_http_methods(["POST", "GET"])
def logout_view(request):
    # Prefer POST
    if request.method == "POST":
        logout(request)

        return render(request, "accounts/login.html")

    logout(request)
    return render(request, "accounts/login.html")