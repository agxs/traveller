from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'trading.views.tradingCore'),
    url(r'^tradingCore$', 'trading.views.tradingCore'),
    url(r'^tradingPassenger$', 'trading.views.tradingPassenger'),
    url(r'^tradingSelectPassenger$', 'trading.views.tradingSelectPassenger'),
    
    url(r'^mock$', 'trading.views.mock'),
)
