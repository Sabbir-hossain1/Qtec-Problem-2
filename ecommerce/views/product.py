from django.shortcuts import render

from ecommerce.models import Product


def products(request):
    context = {"products": Product.objects.all()}
    return render(request, 'ecommerce/product/index.html', context)