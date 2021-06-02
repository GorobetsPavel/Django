from django.shortcuts import render
from .models import Product


def products(request, pk=None):
    title = 'каталог/продукты'

    if pk:
        product = Product.objects.get(pk=pk)
        context = {
            'product': product
        }
        return render(request, 'mainapp/product.html', context=context)

    links_menu =[
        {'href': 'mainapp:index', 'name': 'все'},
        {'href': 'mainapp:index', 'name': 'дом'},
        {'href': 'mainapp:index', 'name': 'офис'},
        {'href': 'mainapp:index', 'name': 'модерн'},
        {'href': 'mainapp:index', 'name': 'классика'},
    ]
    context = {
        'links_menu': links_menu,
        'title': title,
    }
    return render(request, 'mainapp/products.html', context=context)
