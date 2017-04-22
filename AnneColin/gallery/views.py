# coding: utf-8

import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.template.loader import get_template
from django.template import Context
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

from gallery.models import Category, Picture, Format, Message
from gallery.forms import ContactForm
from AnneColin import settings


class IndexView(generic.ListView):
    template_name = u'gallery/index.html'
    context_object_name = u'categories'

    def get_queryset(self):
        return Category.objects.all()


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all().order_by(u'pub_date')

    previous_cat = Category.objects.filter(pub_date__lt=category.pub_date).order_by(u'-pub_date').first()
    next_cat = Category.objects.filter(pub_date__gt=category.pub_date).order_by(u'pub_date').first()

    pictures = category.picture_set.all()
    return render(request, u'gallery/category.html',
                  {u'category': category,
                   u'categories': categories,
                   u'previous_cat': previous_cat,
                   u'next_cat': next_cat,
                   u'pictures': pictures,
                  })


def picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    pictures = picture.category.picture_set.all().order_by(u'pub_date')[:12]

    previous_pic = Picture.objects.filter(
        category__id=picture.category.id,
        pub_date__lt=picture.pub_date
    ).order_by(u'-pub_date').first()
    next_pic = Picture.objects.filter(
        category__id=picture.category.id,
        pub_date__gt=picture.pub_date
    ).order_by(u'pub_date').first()

    return render(request, u'gallery/picture.html',
                  {
                      u'picture': picture,
                      u'pictures': pictures,
                      u'previous_pic': previous_pic,
                      u'next_pic': next_pic,
                  })


def prices(request):
    return render(request, u'gallery/prices.html', {u'prices': Format.objects.all()})


def contact(request):
    if request.method == u"POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.data
            context = {
                u'name': data[u'name'],
                u'email': data[u'email'],
                u'subject': data[u'subject'],
                u'message': data[u'message'],
            }

            # Send email
            subject = data[u'subject']
            from_email = u"{0} <{1}>".format(data[u'name'], context[u'email'])
            message_html = get_template(u"gallery/email/contact.html").render({'context': Context(context)})
            message_txt = get_template(u"gallery/email/contact.txt").render({'context': Context(context)})
            msg = EmailMultiAlternatives(
                subject,
                message_txt,
                from_email,
                [settings.MAIL_CONTACT])
            msg.attach_alternative(message_html, u"text/html")
            msg_base = Message()
            msg_base.date = datetime.datetime.now().isoformat()
            msg_base.name = data[u'name']
            msg_base.email = data[u'email']
            msg_base.subject = data[u'subject']
            msg_base.message = data[u'message']
            msg_base.save()
            try:
                msg.send()
                messages.success(request, u"Votre message a bien été envoyé.")
            except:
                msg = None
                messages.error(request, u"Une erreur est survenue.")

            # reset the form after successful validation
            form = ContactForm()
        return render(request, u"gallery/contact.html", {u"form": form})

    form = ContactForm()

    return render(request, u'gallery/contact.html', {u"form": form})
