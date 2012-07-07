from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'trading.views.index'),
    url(r'^receiveInitial$', 'trading.views.receiveInitial'),
    url(r'^rollForPassengers$', 'trading.views.rollForPassengers'),
    
    url(r'^mock$', 'trading.views.mock'),
)
