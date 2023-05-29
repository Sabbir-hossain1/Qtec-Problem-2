from django.urls import path

from .views import product

app_name = 'ecommerce'
urlpatterns = [
    path('checkbox-filter/', product.checkbox_filter, name='checkbox_filter'),
    path('', product.products, name='products'),
    path('products/', product.all_products_search, name='all_products_search'),
    path('category/<category_id>/', product.category_wise_products, name='category_wise_products'),
    path('category/<category_id>/products/', product.filtered_category_products, name='filtered_category_products'),
]
