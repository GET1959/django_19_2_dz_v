from django.shortcuts import render

from catalog.models import Product, Category


def index(request):
    return render(request, 'catalog/index.html')


def home(request):
    context = {
        'object_list': Product.objects.all()[:3]
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"name - {name}, phone - {phone}, message - {message}")
    return render(request, 'catalog/contacts.html')


def product(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/product.html', context)


def product_item(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }

    return render(request, 'catalog/product_item.html', context)


def category(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'base.html', context)


# def category_item(request, pk):
#     cat_item = Category.objects.get(pk=pk)
#     context = {
#         'object': Product.objects.filter(category_id=pk),
#         'title': f'Категория {cat_item}',
#     }
#
#     return render(request, 'catalog/categories.html', context)


def beverages(request):
    context = {
        'object_list': Product.objects.filter(category=1)
    }
    return render(request, 'catalog/product.html', context)


def condiments(request):
    context = {
        'object_list': Product.objects.filter(category=2)
    }
    return render(request, 'catalog/product.html', context)


def confections(request):
    context = {
        'object_list': Product.objects.filter(category=3)
    }
    return render(request, 'catalog/product.html', context)
