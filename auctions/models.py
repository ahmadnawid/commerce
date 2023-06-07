from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.categoryName}"



class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    image = models.ImageField(upload_to='img')
    status = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

class Watchlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ManyToManyField(Listing)
   def __str__(self):
       return f"{self.user}'s WatchList"

class Bid(models.Model):
    currentbid = models.IntegerField()
    numofbids = models.IntegerField(default=1)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_id")

