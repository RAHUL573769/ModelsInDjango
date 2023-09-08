from django.shortcuts import render
from django.shortcuts import redirect
from . import models


# Create your views here.
def homepage(request):
    return render(request, "base.html")


def homepagetemplate(request):
    student = models.Student.objects.all()
    print(student)
    return render(request, "home.html", {"data": student})


def delete_user(request, roll):
    std = models.Student.objects.get(pk=roll).delete()
    print(std)
    student = models.Student.objects.all()
    return redirect("home")
