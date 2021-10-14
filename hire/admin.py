from django.contrib import admin
from django.contrib.admin.decorators import display
from hire.models import ItemforHire

class HireAdmin(admin.ModelAdmin):
    list_display=('product_name', 'product_details', 'contact_number','product_price', 'product_stock', 'product_condition','hire_duration','product_location')

    class Meta:
        model=ItemforHire
admin.site.register(ItemforHire,HireAdmin)
