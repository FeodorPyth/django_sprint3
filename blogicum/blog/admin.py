from django.contrib import admin

from .models import Post, Category, Location


@admin.register(Post, Category, Location)
class CommonAdmin(admin.ModelAdmin):
    pass
