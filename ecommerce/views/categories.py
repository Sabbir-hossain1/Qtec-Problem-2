from django.shortcuts import render


def categories(request):
    return render(request, 'ecommerce/categories/index.html')