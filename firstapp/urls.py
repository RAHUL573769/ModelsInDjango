from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("home/", views.homepage),
    path("hometemplate/", views.homepagetemplate),
    path("delete/<int:roll>", views.delete_user, name="delete_student"),
]
