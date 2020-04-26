from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import MenuForm
from .models import MenuCategory, Menus
from django.contrib import messages


def home(request):
    template = loader.get_template("hotel/base.html")
    context = {"page_name": "home"}
    return HttpResponse(template.render(context, request))


def menu(request):
    template = loader.get_template("hotel/base.html")
    context = {
        "page_name": "menus",
        "form": MenuForm,
        "menus": Menus.objects.all()
    }
    return HttpResponse(template.render(context, request))


def add_menu(request):
    try:
        if request.method == "POST":
            menu_data = Menus(
                menu_name=request.POST['menu_name'],
                menu_description=request.POST['menu_description'],
                menu_category=MenuCategory.objects.get(category=request.POST['menu_category']),
                menu_price=request.POST['menu_price']
            )
            menu_data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        raise e
