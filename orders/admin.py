from django.contrib import admin
from .models import Status, Client, Order, DetailOrder


admin.site.register(Status)
admin.site.register(Client)

class DetailOrderInline(admin.TabularInline):
    model = DetailOrder

class OrderAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)
    inlines = [DetailOrderInline]

admin.site.register(Order, OrderAdmin)