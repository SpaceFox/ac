# coding: utf-8

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import generic

from gallery.models import Category, Picture

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.all()

def category(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    categories = Category.objects.all()
    pictures = category.picture_set.all()
    return render(request, 'gallery/category.html',
                    {   'category'   : category,
                        'categories' : categories,
                        'pictures'   : pictures,
                    })

def picture(request, picture_id):
    picture = get_object_or_404(Picture, pk = picture_id)
    pictures = picture.category.picture_set.all()
    return render(request, 'gallery/picture.html',
                    {
                        'picture'    : picture,
                        'pictures'   : pictures,
                    })