# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'reestr'

urlpatterns = [
    #/reestr/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /reestr/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /reestr/album/2/update
    url(r'^(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /reestr/album/2/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /reestr/export/xls
    url(r'export/xls/$', views.export_users_xls, name='export_reestr_xls'),

    # /reestr/irpin
    url(r'irpin/$', views.IrpinView.as_view(), name='irpin'),
]

