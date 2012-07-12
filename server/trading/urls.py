from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'trading.views.tradingCore'),
    url(r'^tradingCore$', 'trading.views.tradingCore'),
    url(r'^tradingPassenger$', 'trading.views.tradingPassenger'),
    url(r'^tradingSelectPassenger$', 'trading.views.tradingSelectPassenger'),
    url(r'^tradingMail$', 'trading.views.tradingMail'),
    url(r'^tradingSpeculative$', 'trading.views.tradingSpeculative'),
    url(r'^tradingSelectSpeculative$', 'trading.views.tradingSelectSpeculative'),
    url(r'^tradingSelectFreight$', 'trading.views.tradingSelectFreight'),
    url(r'^tradingNegotiateTradeGood$', 'trading.views.tradingNegotiateTradeGood'),
    
    url(r'^mock$', 'trading.views.mock'),
)
