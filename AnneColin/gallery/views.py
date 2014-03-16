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
    category        = get_object_or_404(Category, pk = category_id)
    categories      = Category.objects.all().order_by('pub_date')
    
    # Django 1.5 --> Pas encore first()
    try:
        previous_cat = Category.objects.filter(pub_date__lt = category.pub_date).order_by('-pub_date')[0]
    except IndexError:
        previous_cat = None
    try:
        next_cat = Category.objects.filter(pub_date__gt = category.pub_date).order_by('pub_date')[0]
    except IndexError:
        next_cat = None
        
    pictures = category.picture_set.all()
    return render(request, 'gallery/category.html',
                    {   'category'      : category,
                        'categories'    : categories,
                        'previous_cat'  : previous_cat,
                        'next_cat'      : next_cat,
                        'pictures'       : pictures,
                    })

def picture(request, picture_id):
    picture = get_object_or_404(Picture, pk = picture_id)
    pictures = picture.category.picture_set.all().order_by('pub_date')[:12]
    
    # Django 1.5 --> Pas encore first()
    try:
        previous_pic = Picture.objects.filter(category__id = picture.category.id, pub_date__lt = picture.pub_date).order_by('-pub_date')[0]
    except IndexError:
        previous_pic = None
    try:
        next_pic = Picture.objects.filter(category__id = picture.category.id, pub_date__gt = picture.pub_date).order_by('pub_date')[0]
    except IndexError:
        next_pic = None
        
    return render(request, 'gallery/picture.html',
                    {
                        'picture'       : picture,
                        'pictures'      : pictures,
                        'previous_pic'  : previous_pic,
                        'next_pic'      : next_pic,
                    })