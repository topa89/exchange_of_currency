from django.contrib import admin

from .models import LimitVal
from orders.models import Orders

class LimitAdmin(admin.ModelAdmin):
    list_display = ('name', 'index', 'reserve')


admin.site.register(LimitVal, LimitAdmin)
admin.site.register(Orders)

