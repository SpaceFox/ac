from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):

    name = models.CharField('Nom', max_length=80)
    icon = models.ImageField('Icône', upload_to='categories')
    description = models.TextField('Description', blank=True, null=True)
    pub_date = models.DateTimeField('Date de publication', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Format(models.Model):
    name = models.CharField('Nom', max_length=80)
    description = models.TextField('Description', null=True)
    price = models.DecimalField('Prix', max_digits=7, decimal_places=2)

    def __str__(self):
        return '{} ({:10.2f} €)'.format(self.name, self.price)


class Picture(models.Model):

    category = models.ForeignKey(Category)
    formats = models.ManyToManyField(Format)
    title = models.CharField('Titre', max_length=80)
    image = models.ImageField('Image', upload_to='pictures')
    description = models.TextField('Description', blank=True, null=True)
    pub_date = models.DateTimeField('Date de publication', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('picture', kwargs={'picture_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

class Message(models.Model):

    date = models.DateTimeField('Date')
    name = models.CharField('Nom', max_length=200)
    email = models.CharField('Email', max_length=250)
    subject = models.CharField('Sujet', max_length=200)
    message = models.TextField('Message')

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"