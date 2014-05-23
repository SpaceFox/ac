from django.contrib import admin

from gallery.models import Category, Format, Picture, Price


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    pass


class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')
    list_filter = ['category']
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Format)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Price)
