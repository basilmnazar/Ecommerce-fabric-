# Generated by Django 4.2.7 on 2023-11-22 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_alter_fabric_fabric_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('price', models.FloatField(null=True)),
                ('is_ordered', models.BooleanField(default=False, null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.fabric')),
            ],
        ),
        migrations.CreateModel(
            name='cart_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='myapp.cart_item')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
