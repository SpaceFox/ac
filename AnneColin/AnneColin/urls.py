from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap

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

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('gallery.urls')),

                       # Static
                       (r'^expositions/', TemplateView.as_view(template_name="gallery/expositions.html")),

                       # Sitemaps
                       (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
