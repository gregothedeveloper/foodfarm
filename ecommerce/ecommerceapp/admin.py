from django.contrib import admin
from ecommerceapp.models import  Contact,Product,Order,OrderUpdate
# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderUpdate)