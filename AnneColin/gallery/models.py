# coding: utf-8

from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.dispatch.dispatcher import receiver
import os


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        
    name        = models.CharField(max_length = 80)
    slug        = models.SlugField(max_length = 80)
    icon_aside  = models.ImageField(upload_to = 'categories/aside', blank = True)
    icon_full   = models.ImageField(upload_to = 'categories/full')
    description = models.TextField(blank = True, null = True)
    pub_date    = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.name

    def save(self, force_update=False, force_insert=False):
        if has_changed(self, 'icon_full') and self.icon_full :
            # TODO : delete old image
            
            image = Image.open(self.icon_full)
            
            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')
            
            resize_image(image, (90, 60), self.icon_aside)
            resize_image(image, (165, 165), self.icon_full)
            
            # save the image object
            super(Category, self).save(force_update, force_insert)
        else :
            super(Category, self).save()

class Format(models.Model):
    name        = models.CharField(max_length = 80)
    description = models.TextField(null = True)

class Picture(models.Model):
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    
    category        = models.ForeignKey(Category)
    formats         = models.ManyToManyField(Format, through = 'Price')
    title           = models.CharField(max_length = 80)
    slug            = models.SlugField(max_length = 80)
    image_aside     = models.ImageField(upload_to = 'pictures/aside', blank = True)
    image_category  = models.ImageField(upload_to = 'pictures/category', )
    image_full      = models.ImageField(upload_to = 'pictures/full')
    description     = models.TextField(blank = True, null = True)
    pub_date        = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.title

    def save(self, force_update=False, force_insert=False):
        if has_changed(self, 'image_full') and self.image_full :
            # TODO : delete old image
            
            image = Image.open(self.image_full)
            
            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')
                
            resize_image(image, (90, 60), self.image_aside)
            resize_image(image, (165, 165), self.image_category)
            resize_image(image, (900, 600), self.image_full)
            
            # save the image object
            super(Image, self).save(force_update, force_insert)
        else :
            super(Image, self).save()
    
class Price(models.Model):
    picture = models.ForeignKey(Picture)
    format  = models.ForeignKey(Format)
    value   = models.IntegerField()
    
    
def resize_image(image, size, dest_field):
    
    image.thumbnail(size, Image.ANTIALIAS)
    
    # save the thumbnail to memory
    temp_handle = StringIO()
    image.save(temp_handle, 'JPEG', quality=90)
#    temp_handle.seek(0)  # rewind the file
    
    # save to the thumbnail field
    suf = SimpleUploadedFile(dest_field.name,
                             temp_handle.read(),
                             content_type='image/jpeg')
    dest_field.save(suf.name, suf, save=False)
    

def has_changed(instance, field, manager='objects'):
    """Returns true if a field has changed in a model
    May be used in a model.save() method.
    """
    if not instance.pk:
        return True
    manager = getattr(instance.__class__, manager)
    old = getattr(manager.get(pk=instance.pk), field)
    return not getattr(instance, field) == old

# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=Category)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes image from filesystem
    when corresponding object is deleted.
    """
    if instance.physical:
        if os.path.isfile(instance.physical.path):
            os.remove(instance.physical.path)
