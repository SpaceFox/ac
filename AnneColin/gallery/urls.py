from django.conf.urls import url

from gallery import views

urlpatterns = [
   url(r'^$', views.IndexView.as_view(), name='index'),
   url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
   url(r'^picture/(?P<picture_id>\d+)/$', views.picture, name='picture'),
   url(r'^prices/$', views.prices),
   url(r'^contact/$', views.contact),
]
