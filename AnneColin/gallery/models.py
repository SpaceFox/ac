from django.db import models

# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length = 80)
    slug        = models.SlugField(max_length = 80)
    icon        = models.ImageField(upload_to = 'categories')
    description = models.TextField(blank = True, null = True)
    pub_date    = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.name

class Format(models.Model):
    name        = models.CharField(max_length = 80)
    description = models.TextField(null = True)

class Picture(models.Model):
    category    = models.ForeignKey(Category)
    formats     = models.ManyToManyField(Format, through = 'Price')
    title       = models.CharField(max_length = 80)
    slug        = models.SlugField(max_length = 80)
    image       = models.ImageField(upload_to = 'pictures')
    description = models.TextField(blank = True, null = True)
    pub_date    = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.title
    
class Price(models.Model):
    picture = models.ForeignKey(Picture)
    format  = models.ForeignKey(Format)
    value   = models.IntegerField()
