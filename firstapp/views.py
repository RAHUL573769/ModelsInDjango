from django.shortcuts import render

from . import models


# Create your views here.
def homepage(request):
    return render(request, "base.html")


def homepagetemplate(request):
    student = models.Student.objects.all()
    print(student)
    return render(request, "home.html", {"data": student})
