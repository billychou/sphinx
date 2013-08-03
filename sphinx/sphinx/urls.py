#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'note.views.index'),
    url(r'^$', 'note.views.index'),
    )

urlpatterns += patterns('',
    url(r'^(\w{6,12})$', 'note.views.noteprocess'),
    url(r'^share/(\w{6,12})$', 'note.views.shareprocess'),
)
