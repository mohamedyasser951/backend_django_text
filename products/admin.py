from django.contrib import admin
from .models import product,Test
# Register your models here.




class ProductConfiq(admin.ModelAdmin):
    list_display =["name","price","active",'category',]
    list_display_links = ["name"]
    list_editable = ["price","active",'category']
    search_fields = ["name"]
    list_filter = ["category"]
    fields = ["name","price"]

admin.site.register(product,ProductConfiq)
admin.site.register(Test)