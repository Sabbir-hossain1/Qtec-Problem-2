from django.urls import path

from .views import product

app_name = 'ecommerce'
urlpatterns = [
    path('', product.products, name='products')
]
