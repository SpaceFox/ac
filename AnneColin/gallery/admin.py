# coding: utf-8

from django.contrib import admin

from gallery.models import Category, Format, Picture, Message


class CategoryAdmin(admin.ModelAdmin):
    list_display = (u'name', u'pub_date')
    pass


class PictureAdmin(admin.ModelAdmin):
    list_display = (u'title', u'category', u'pub_date')
    list_filter = [u'category']
    pass


class FormatAdmin(admin.ModelAdmin):
    list_display = (u'name', u'price')
    pass


class MessageAdmin(admin.ModelAdmin):
    list_display = (u'name', u'date', u'email', u'subject')
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Message, MessageAdmin)
