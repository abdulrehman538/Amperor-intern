from django.shortcuts import redirect, render

from .models import Person


def home(request):
    result = None
    searched = False

    if request.method == "POST":
        searched = True
        ids = request.POST.get("id")

        if ids:
            try:
                result = Person.objects.get(id=int(ids))
            except (Person.DoesNotExist, ValueError):
                result = None

    return render(request, "home.html", {"result": result, "searched": searched})


def about(request):
    people = Person.objects.all()
    return render(request, "about.html", {"people": people})


def login_view(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email == "abdule" and password == "konan":
            return redirect("home")

        error = "Invalid credentials"

    return render(request, "login.html", {"error": error})
