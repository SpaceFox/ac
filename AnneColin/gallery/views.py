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
    template_name = 'gallery/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all().order_by('pub_date')

    previous_cat = Category.objects.filter(pub_date__lt=category.pub_date).order_by('-pub_date').first()
    next_cat = Category.objects.filter(pub_date__gt=category.pub_date).order_by('pub_date').first()

    pictures = category.picture_set.all()
    return render(request, 'gallery/category.html',
                  {'category': category,
                   'categories': categories,
                   'previous_cat': previous_cat,
                   'next_cat': next_cat,
                   'pictures': pictures,
                  })


def picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    pictures = picture.category.picture_set.all().order_by('pub_date')[:12]

    previous_pic = Picture.objects.filter(
        category__id=picture.category.id,
        pub_date__lt=picture.pub_date
    ).order_by('-pub_date').first()
    next_pic = Picture.objects.filter(
        category__id=picture.category.id,
        pub_date__gt=picture.pub_date
    ).order_by('pub_date').first()

    return render(request, 'gallery/picture.html',
                  {
                      'picture': picture,
                      'pictures': pictures,
                      'previous_pic': previous_pic,
                      'next_pic': next_pic,
                  })


def prices(request):
    return render(request, 'gallery/prices.html', {'prices': Format.objects.all()})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.data
            context = {
                'name': data['name'],
                'email': data['email'],
                'subject': data['subject'],
                'message': data['message'],
            }

            # Send email
            subject = data['subject']
            from_email = "{0} <{1}>".format(data['name'], context['email'])
            message_html = get_template("gallery/email/contact.html").render(Context(context))
            message_txt = get_template("gallery/email/contact.txt").render(Context(context))
            msg = EmailMultiAlternatives(
                subject,
                message_txt,
                from_email,
                [settings.MAIL_CONTACT])
            msg.attach_alternative(message_html, "text/html")
            msg_base = Message()
            msg_base.date = datetime.datetime.now().isoformat()
            msg_base.name = data['name']
            msg_base.email = data['email']
            msg_base.subject = data['subject']
            msg_base.message = data['message']
            msg_base.save()
            try:
                msg.send()
                messages.success(request, u"Votre message a bien été envoyé.")
            except:
                msg = None
                messages.error(request, "Une erreur est survenue.")

            # reset the form after successful validation
            form = ContactForm()
        return render(request, "gallery/contact.html", {"form": form})

    form = ContactForm()

    return render(request, 'gallery/contact.html', {"form": form})
