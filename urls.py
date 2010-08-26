#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.conf.urls.defaults import *

from views import convert_file
from views import download_xform

# all paths are relative to the django project

urlpatterns = patterns('',
                       (r'^$',                          convert_file),
                       (r'^sm/(?P<path>.*)$',          'django.views.static.serve', {'document_root': 'xls2xform/webcontent'}),
                       (r'^example_xls/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'xls2xform/example_xls'}),
                       (r'^(?P<path>submissions/.*)$',  download_xform)
                       )
