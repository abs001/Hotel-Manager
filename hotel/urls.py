from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="index"),
    path("menus/", views.menu, name="menus"),
    path("add_menu/", views.add_menu, name="add_menu")
]