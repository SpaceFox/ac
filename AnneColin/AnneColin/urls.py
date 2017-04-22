from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from gallery.models import Category, Picture


# SiteMap data
sitemaps = {
    'categories': GenericSitemap(
        {'queryset': Category.objects.all(), 'date_field': 'pub_date'},
        changefreq='monthly',
        priority=0.7
    ),
    'pictures': GenericSitemap(
        {'queryset': Picture.objects.all(), 'date_field': 'pub_date'},
        changefreq='weekly',
        priority=0.7
    ),
}

admin.autodiscover()

urlpatterns = [

   url(r'^admin/', include(admin.site.urls)),
   url(r'^', include('gallery.urls')),

   # Static
   url(r'^expositions/', TemplateView.as_view(template_name="gallery/expositions.html")),

   # Sitemaps
   url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
