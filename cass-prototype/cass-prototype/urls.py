from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^$', 'reddit.views.home', name='home'),
    url(r'^api/', include(patterns('',
        url(r'^reddit/', include('reddit.api.urls', namespace='reddit')),
        ), namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
