from ..models import Menu


def get_menus():
    menus = Menu.objects.all()
    return menus


def get_menu(menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    return menu


def update_menu(menu_pk, new_menu):
    menu = Menu.objects.get(pk=menu_pk)
    menu.name = new_menu.name
    menu.comercio = new_menu.comercio
    menu.save()
    return menu


def delete_menu(menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    menu.delete()


def create_menu(new_menu):
    menu = Menu(new_menu)
    menu.save()
    return menu
