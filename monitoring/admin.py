from django.contrib import admin
from .models import Stocklog, Saleslog, UserActivitylog


@admin.register(Stocklog)
class StocklogAdmin(admin.ModelAdmin):
    list_display = ['product', 'old_stock', 'new_stock', 'changed_at']
    readonly_fields = ['product', 'old_stock', 'new_stock', 'changed_at']


@admin.register(Saleslog)
class SaleslogAdmin(admin.ModelAdmin):
    list_display = ['period', 'total_sales']
    readonly_fields = ['period', 'total_sales']


@admin.register(UserActivitylog)
class UserActivitylogAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity']
    list_filter = ['activity']
    readonly_fields = ['user', 'activity']