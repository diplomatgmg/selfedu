from django.contrib import admin

from apps.women.models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
