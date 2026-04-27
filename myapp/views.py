from django.shortcuts import render
from .models import Person   # 👈 import model

def home(request):
    result = None

    if request.method == "POST":
        ids = request.POST.get("id")

        if ids:
            try:
                result = Person.objects.get(id=int(ids))   # 👈 THIS LINE
            except Person.DoesNotExist:
                result = None

    return render(request, "home.html", {"result": result})