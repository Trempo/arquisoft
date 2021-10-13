from comercios.models import Comercio
from ..models import Menu


def get_menus(comercio_pk):
    menus = Menu.objects.filter(comercio=comercio_pk)
    return menus


def get_menu(menu_pk):
    menu = Menu.objects.filter(pk=menu_pk)
    return menu


def update_menu(menu_pk, new_menu):
    comercio = Comercio.objects.get(pk=new_menu['comercio'])
    menu = Menu.objects.get(pk=menu_pk)
    menu.name = new_menu['name']
    menu.comercio = comercio
    menu.save()
    return menu


def delete_menu(menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    menu.delete()


def create_menu(new_menu):
    comercio = Comercio.objects.get(pk = new_menu['comercio'])
    menu = Menu(name=new_menu['name'], comercio=comercio)
    menu.save()
    return menu
