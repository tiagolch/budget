from django.contrib import admin
from .models import Revenue, Expense, Actor, Card, Category


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'value',
    ]


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'value',
        'start_date',
        'end_date',
    ]
    list_display_links = ['name', 'description']
    list_filter = [
        'start_date',
        'end_date',
        'fixed_expense',
        'category',
    ]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'active',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'description',
    ]
