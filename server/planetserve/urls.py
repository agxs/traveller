from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'planetserve.views.index'),
    url(r'^(?P<planet_id>\d+)/$', 'planetserve.views.detail'),
)
