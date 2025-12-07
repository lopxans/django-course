from django.contrib import admin
from .models import *

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'published', 'user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'published', 'user']

@admin.register(Song)  # ✔ FIXED HERE
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'duration', 'written_by']
