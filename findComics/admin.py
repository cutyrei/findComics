from django.contrib import admin
from .models import Comic

class ComicAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']

admin.site.register(Comic, ComicAdmin)
