from django.urls import path

from .views import categories

app_name = 'ecommerce'
urlpatterns = [
    path('', categories.categories, name='categories')
]
