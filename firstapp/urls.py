from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("home/", views.homepage),
    path("hometemplate/", views.homepagetemplate),
]
