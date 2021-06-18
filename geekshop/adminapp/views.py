from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'
    users_list = ShopUser.objects.filter(is_delete=False).order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()

            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'
    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserRegisterForm(instance=edit_user)

    context = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_delete = True
        user.save()

        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории/создание'

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        edit_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории/редактирование'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES, instance=category)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:category_update', args=[category.pk]))
    else:
        edit_form = ShopUserRegisterForm(instance=category)

    context = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/category_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории/удаление'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_delete = True
        user.save()

        return HttpResponseRedirect(reverse('admin_staff:categories'))

    context = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/category_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукты/создание'

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:products'))
    else:
        edit_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукты/редактирование'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES, instance=product)
        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:product_update', args=[product.pk]))
    else:
        edit_form = ShopUserRegisterForm(instance=product)

    context = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/product_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'продукты/удаление'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_delete = True
        product.save()

        return HttpResponseRedirect(reverse('admin_staff:products'))

    context = {
        'title': title,
        'product_to_delete': product,
    }

    return render(request, 'adminapp/product_delete.html', context)
