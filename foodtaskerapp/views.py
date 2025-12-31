from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # reload home after login
        else:
            return render(request, "register.html", {
                "error": "Invalid username or password"
            })

    return render(request, "home.html")