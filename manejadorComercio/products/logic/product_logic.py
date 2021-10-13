from comercios.models import Comercio
from menus.models import Menu
from products.models import Product


def get_products(menu_pk):
    products = Product.objects.filter(menu=menu_pk)
    return products


def get_product(product_pk):
    product = Product.objects.filter(pk=product_pk)
    return product


def update_product(product_pk, new_product):
    menu = Menu.objects.get(pk=new_product['menu'])
    product = Product.objects.get(pk=product_pk)
    product.menu = menu
    product.name = new_product['name']
    product.price = new_product['price']
    product.stock = new_product['stock']
    product.save()
    return product


def delete_product(product_pk):
    product = Product.objects.get(pk=product_pk)
    product.delete()


def create_product(new_product):
    menu = Menu.objects.get(pk = new_product['menu'])
    product = Product(menu = menu, name = new_product['name'], price = new_product['price'], stock = new_product['stock'])
    product.save()
    return product
