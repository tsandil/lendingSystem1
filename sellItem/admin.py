from django.contrib import admin
from django.contrib.admin.decorators import display
from sellItem.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','contact_number')

    class Meta:
        model=Item
admin.site.register(Item,ItemAdmin)
