from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^entry$', views.entry),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url('^user_account/(?P<id>[0-9]+)/$', views.view_account),
    url(r'^user_account/(?P<id>[0-9]+)/edit$', views.edit_account),
    url(r'^update_account/(?P<id>[0-9]+)$', views.update_account),
    url(r'^logout$', views.logout)
]