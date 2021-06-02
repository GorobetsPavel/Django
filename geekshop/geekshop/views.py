from django.shortcuts import render
from mainapp.models import Product


def index(request, pk=None):

    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'products': products,
        'title': title,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    return render(request, 'geekshop/contact.html')


