#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from note.models import Notepad

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sphinx.views.home', name='home'),
    # url(r'^sphinx/', include('sphinx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'note.views.index'),
    url(r'^$', 'note.views.index'),
    )

urlpatterns += patterns('',
    url(r'^(\w{6,12})$', 'note.views.noteprocess'),
)
