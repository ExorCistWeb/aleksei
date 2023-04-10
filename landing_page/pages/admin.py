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


"""class IndividualAdmin(admin.ModelAdmin):
    list_display = ('time', 'price')
admin.site.register(Individual) 

#Individual_consultation
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('time', 'price')
admin.site.register(Family) 
#Family_consultation

#Consultation_subscription5
class Subscription5Admin(admin.ModelAdmin):
    list_display = ('time', 'price','discount')
admin.site.register(Subscription5) 

#Consultation_subscription10

class Subscription10Admin(admin.ModelAdmin):
    list_display = ('time', 'price','discount')
admin.site.register(Subscription10) 

#Consultation_subscription15
class Subscription15Admin(admin.ModelAdmin):
    list_display = ('time', 'price','discount')
admin.site.register(Subscription15) """
