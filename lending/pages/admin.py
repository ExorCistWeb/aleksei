from django.contrib import admin
from .models import Image, Post, Subscription#Individual,Family,Subscription5 #,Subscription10,Subscription15

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'data', 'subject', 'text' )
admin.site.register(Image, ImageAdmin) 
#image


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','time', 'price' )
admin.site.register(Post, PostAdmin) 


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id','time', 'price', 'text', 'maney' )
admin.site.register(Subscription, SubscriptionAdmin)