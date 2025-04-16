from django.contrib import admin

# Register your models here.

# admin.site.register(Author)

admin.site.register(Kitchen)




@admin.register(Kitchen)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'reipe')
    list_display_links = ('name', 'recipe')
    list_filter = ('name', 'surname', 'recipe')
    search_fields = ('name', 'surname')
    ordering = ('id', 'name', 'surname')



admin.site.register(Proposal)