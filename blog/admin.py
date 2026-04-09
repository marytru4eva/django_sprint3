from django.contrib import admin
from .models import Location, Category, Post


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'description', 'is_published')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'location', 'pub_date', 'is_published'
    )
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'text')
