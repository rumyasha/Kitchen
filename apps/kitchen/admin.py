from django.contrib import admin

# Register your models here.

from apps.kitchen.models import *

# admin.site.register(Author)
admin.site.register(Task)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'recipe')
    list_display_links = ('name', 'recipe')
    list_filter = ('name', 'surname', 'recipe')
    search_fields = ('name', 'surname')
    ordering = ('id', 'name', 'surname')

admin.site.register(Proposal)



