from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads', blank=True, null = True)
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    balace_after = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    return_date = models.DateTimeField(null=True, blank=True, default=None)
    buy_book = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
    

class BorroBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.purchase_date)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    rating = models.IntegerField(default=0)
    comment = models.TextField(  null=True)


 
    
