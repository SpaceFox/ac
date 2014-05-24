# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):

    name = models.CharField(u'Nom', max_length=80)
    icon = models.ImageField(u'Icône', upload_to='categories')
    description = models.TextField(u'Description', blank=True, null=True)
    pub_date = models.DateTimeField(u'Date de publication', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.id})

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Catégorie"
        verbose_name_plural = u"Catégories"


class Format(models.Model):
    name = models.CharField(u'Nom', max_length=80)
    description = models.TextField(u'Description', null=True)
    price = models.DecimalField(u'Prix', max_digits=7, decimal_places=2)

    def __unicode__(self):
        return u'{} ({:10.2f} €)'.format(self.name, self.price)


class Picture(models.Model):

    category = models.ForeignKey(Category)
    formats = models.ManyToManyField(Format)
    title = models.CharField(u'Titre', max_length=80)
    image = models.ImageField(u'Image', upload_to='pictures')
    description = models.TextField(u'Description', blank=True, null=True)
    pub_date = models.DateTimeField(u'Date de publication', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('picture', kwargs={'picture_id': self.id})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Image"
        verbose_name_plural = u"Images"
