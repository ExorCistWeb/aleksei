from django.contrib import admin
from .models import Image,Individual_consultation,Family_consultation,Consultation_subscription5,Consultation_subscription10,Consultation_subscription15

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'data', 'subject', 'text' )
admin.site.register(Image, ImageAdmin) 
#image

class Individual_consultationAdmin(admin.ModelAdmin):
    list_display = ('time', 'price')
admin.site.register(Individual_consultation) 

#Individual_consultation
class Family_consultationAdmin(admin.ModelAdmin):
    list_display = ('time', 'price')
admin.site.register(Family_consultation) 
#Family_consultation

#Consultation_subscription5
class Consultation_subscription5Admin(admin.ModelAdmin):
    list_display = ('time', 'price','discount')
admin.site.register(Consultation_subscription5) 

#Consultation_subscription10
class Consultation_subscription10Admin(admin.ModelAdmin):
    list_display = ('time', 'price','discount')
admin.site.register(Consultation_subscription10) 

#Consultation_subscription15
class Consultation_subscription15Admin(admin.ModelAdmin):
    list_display = ('time', 'price','discount')
admin.site.register(Consultation_subscription15) 
