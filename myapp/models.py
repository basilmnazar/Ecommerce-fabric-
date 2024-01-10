from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class register_user(models.Model):
    address=models.CharField(max_length=255,null=True)
    phone=models.IntegerField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
class fabric(models.Model):
    fabric_image=models.ImageField(upload_to='images/',null=True , blank=True)
    fabric_title=models.CharField(max_length=255)
    fabric_discription=models.CharField(max_length=255)
    fabric_price=models.DecimalField(max_digits=10,decimal_places=2)
    # fabric_color=models.CharField(max_length=255)
    fabric_quantity=models.IntegerField()
    fabric_material=models.CharField(max_length=255)
    def __str__(self):
        return(self.fabric_title)



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(fabric, through='CartItem')

class CartItem(models.Model):
    product = models.ForeignKey(fabric, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)