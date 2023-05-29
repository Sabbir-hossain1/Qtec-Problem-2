from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

from ecommerce.models import Product, Category, Brand, Seller, Warranty


def checkbox_filter(request):
    data = dict()
    category_ids = request.GET.getlist('category_ids[]')
    brand_ids = request.GET.getlist('brand_ids[]')
    seller_ids = request.GET.getlist('seller_ids[]')
    warranty_ids = request.GET.getlist('warranty_ids[]') 
    all_products = Product.objects.all()
    if category_ids:
        all_products = all_products.filter(category__id__in=category_ids)
        print("have cat")
    if brand_ids:
        all_products = all_products.filter(brand__id__in=brand_ids)
        print("have brand")
    if seller_ids:
        all_products = all_products.filter(seller__id__in=seller_ids)
        print("have sel")
    if warranty_ids:
        all_products = all_products.filter(warranty__id__in=warranty_ids)                  
        print("have war")
    data['updated_list'] = render_to_string('ecommerce/product/product_list.html', {"products": all_products})
    return JsonResponse(data)
    




def products(request):
    context = {
        "products": Product.objects.all(),
        "categories": Category.objects.all(),
        "brands": Brand.objects.all(),
        "sellers": Seller.objects.all(),
        "warranties": Warranty.objects.all(),

        }
    return render(request, 'ecommerce/product/index.html', context)


def all_products_search(request):
    data = dict()
    search_text = request.GET.get('search_text')    
    data['updated_list'] = render_to_string('ecommerce/product/product_list.html', {"products":Product.objects.filter(name__icontains=search_text)})
    return JsonResponse(data)


def category_wise_products(request, category_id):
    data = dict()
    selected_category = get_object_or_404(Category, id=category_id)
    data['updated_list'] = render_to_string('ecommerce/product/product_list.html', {"products":Product.objects.filter(category=selected_category)})
    return JsonResponse(data)


def filtered_category_products(request, category_id):
    data = dict()
    search_text = request.GET.get('search_text')
    selected_category = get_object_or_404(Category, id=category_id)
    data['updated_list'] = render_to_string('ecommerce/product/product_list.html', {"products": Product.objects.filter(category=selected_category, name__icontains=search_text)})
    return JsonResponse(data)

    
