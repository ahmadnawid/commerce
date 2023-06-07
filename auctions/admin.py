from django.contrib import admin

# Register your models here.

from .models import Category, Listing, Bid

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "image", "status", "category") 

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "currentbid", "numofbids", "listing") 

# Register your models here.
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)

