from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Warranty(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product/')  

# product Model
class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ManyToManyField(Image)
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='product_brand', on_delete=models.CASCADE)
    warranty = models.ForeignKey(Warranty, related_name='product_warranty', on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, related_name='product_seller', on_delete=models.CASCADE)
    regular_price = models.DecimalField( max_digits=10, decimal_places=2)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name
