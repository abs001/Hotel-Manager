from django import forms
from .models import MenuCategory


def get_menu_category():
    return MenuCategory.objects.all()


class MenuForm(forms.Form):
    menu_name = forms.CharField(label="Menu Name", max_length=100)
    menu_description = forms.CharField(widget=forms.Textarea)
    menu_category = forms.ModelChoiceField(label="Category", queryset=get_menu_category())
    menu_price = forms.FloatField(label="Price")
