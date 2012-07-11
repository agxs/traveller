from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'planetserve.views.index'),
    url(r'^(?P<planet_id>\d+)/$', 'planetserve.views.detail'),
    url(r'^display/(?P<planet_id>\d+)/$', 'planetserve.views.display'),
)
