from django.contrib import admin
from gallery.models import Category, Format, Picture, Price
from sorl.thumbnail.admin import AdminImageMixin

class CategoryAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

class PictureAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Format)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Price)
