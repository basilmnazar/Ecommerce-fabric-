# Generated by Django 4.2.7 on 2023-11-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_fabric_fabric_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabric',
            name='fabric_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
