# coding: utf-8

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from gallery.models import Category

class IndexView(generic.ListView):
    template_name = 'gallery/index.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.all()

def category(request, category_id):
    return HttpResponse("Affichage de la categorie %s" % category_id)

def picture(request, picture_id):
    return HttpResponse("Affichage de l'image %s" % picture_id)