# Generated by Django 4.2.1 on 2023-05-29 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='product/')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(to='ecommerce.image'),
        ),
    ]
