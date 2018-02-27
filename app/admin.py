from django.contrib import admin

from .models import limit_val


class LimnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'index', 'reserve')


admin.site.register(limit_val, LimnitAdmin)
# Register your models here.
