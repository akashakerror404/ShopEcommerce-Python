from django.contrib import admin
from . models import *

# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(categ,catadmin)
#super user akash
#password 1234
class prodAdmin(admin.ModelAdmin):
    list_display =['slug','price','stock','img','available']
    list_editable =['price','stock','img','available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(products,prodAdmin)

