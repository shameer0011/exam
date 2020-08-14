from django.db import models


# Create your models here.
class Offer(models.Model):
    price=models.CharField(max_length = 10)
    img = models.CharField(max_length=258000)

class Catogery(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='image', default='image.jpg')

    def __str__(self):
       return self.name +","+ self.name

class Products(models.Model):
    name=models.CharField(max_length=100)
    image1 =  models.ImageField(upload_to='image2', default='image.jpg')
    price=models.FloatField(max_length=15)
  
    def __str__(self):
       return self.name +","+ self.name
