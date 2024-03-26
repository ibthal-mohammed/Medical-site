from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class News(models.Model):
    username= models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=80)
    body = models.TextField()
    thumb = models.ImageField(blank=True, null=True, default='about-medicine.png')


    def __str__(self):
        return self.title

    def snip(self):
        return self.body[:150]

    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'pk':self.pk})

    def delete_news(self):
        return reverse('news:news_delete', kwargs={'pk':self.pk})        

    def update_news(self):
        return reverse('news:news_update', kwargs={'pk':self.pk})  