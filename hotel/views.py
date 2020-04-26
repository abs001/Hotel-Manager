from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import MenuForm
from .models import MenuCategory, Menus, Tables


def home(request):
    template = loader.get_template("hotel/base.html")
    tables = Tables.objects.all()
    occupied_tables = Tables.objects.filter(occupied=True)
    occupancy = len(occupied_tables)/len(tables)*100
    context = {
        "page_name": "home",
        "tables": tables,
        "occupancy": occupancy
    }
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


def add_table(request):
    try:
        chairs = request.POST["chairs"]
        table = Tables(chairs=chairs)
        table.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        raise e
