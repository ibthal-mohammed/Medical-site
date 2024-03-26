from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Medicine(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)
    thumb = models.ImageField(default='p-6', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

class Cart(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField()
    c_quantity = models.PositiveIntegerField(default=0)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk) + " "+str(self.username)+" "+str(self.medicine)
    
    def get_absolute_url(self):    
        return reverse('medicine:cart_detail', kwargs={'pk': self.pk})

    def updateCart(self):    
        return reverse('medicine:update_cart', kwargs={'pk': self.pk})
    
    def deleteCart(self):    
        return reverse('medicine:delete_cart', kwargs={'pk': self.pk})


class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.pk) + " "+str(self.cart)