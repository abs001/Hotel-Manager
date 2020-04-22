from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template("hotel/base.html")
    context = {"page_name": "home"}
    return HttpResponse(template.render(context, request))


def menu(request):
    template = loader.get_template("hotel/base.html")
    context = {"page_name": "menus"}
    return HttpResponse(template.render(context, request))
