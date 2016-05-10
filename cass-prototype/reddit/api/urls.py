from django.conf.urls import patterns, url

from .views import BlogListCreate, BlogDetail

urlpatterns = patterns(
    '',
    url(r'^blog/$', BlogListCreate.as_view(), name='blog-list-create'),
    url(r'^blog/(?P<uuid>[^/]+)/$', BlogDetail.as_view(), name='blog-detail')
    )
