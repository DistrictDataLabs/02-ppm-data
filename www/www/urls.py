from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^uberjobs/', include('uberjobs.urls', namespace="uberjobs")),
    url(r'^admin/', include(admin.site.urls)),
)
