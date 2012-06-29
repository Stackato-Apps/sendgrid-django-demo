from django.conf.urls import patterns, include, url
from django.shortcuts import redirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^sg/$', 'sg.views.index'),
    (r'^sg/send$', 'sg.views.send'),
    url(r'^$', lambda request: redirect('/sg')),

    # Examples:
    # url(r'^$', 'sgdj.views.home', name='home'),
    # url(r'^sgdj/', include('sgdj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
