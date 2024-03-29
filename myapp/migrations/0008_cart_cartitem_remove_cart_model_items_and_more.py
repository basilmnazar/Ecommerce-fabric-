# Generated by Django 4.1.5 on 2023-11-23 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_cart_item_cart_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fabric')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart_model',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart_model',
            name='user',
        ),
        migrations.DeleteModel(
            name='cart_item',
        ),
        migrations.DeleteModel(
            name='cart_Model',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='myapp.CartItem', to='myapp.fabric'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
