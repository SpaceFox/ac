from django.contrib import admin
from gallery.models import Category, Format, Picture, Price

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'icon_full', 'description']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Format)
admin.site.register(Picture)
admin.site.register(Price)
