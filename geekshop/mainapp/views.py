from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductCategory


def products(request, pk=None):
    title = 'каталог/продукты'

    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        # product = Product.objects.get(pk=pk)
        context = {
            'products': products,
            'title': title,
            'category': category,
            'links_menu': links_menu,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context=context)

    # links_menu =[
    #    {'href': 'mainapp:index', 'name': 'все'},
    #    {'href': 'mainapp:index', 'name': 'дом'},
    #    {'href': 'mainapp:index', 'name': 'офис'},
    #    {'href': 'mainapp:index', 'name': 'модерн'},
    #    {'href': 'mainapp:index', 'name': 'классика'},
    # ]

    products = Product.objects.all()
    context = {
        'links_menu': links_menu,
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context=context)
