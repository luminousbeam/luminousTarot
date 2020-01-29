from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^major_arcana$', views.major_arcana),
    url(r'^major_arcana/(?P<id>[0-9]+)$', views.tarot_meaning),
    url(r'^minor_arcana$', views.minor_arcana),
    url(r'^minor_arcana/(?P<id>[0-9]+)$', views.tarot_meaning),
    url(r'^readings$', views.readings),
    url(r'^readings/three_card$', views.three_card),
    url(r'^readings/three_card/save', views.save_three_card),
    url(r'^readings/four_card$', views.four_card)
]