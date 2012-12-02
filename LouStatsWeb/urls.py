from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^stats/$', 'stats.views.index'),
    url(r'^stats/refresh/$', 'stats.views.refresh'),
    url(r'^stats/graph/$', 'stats.views.graph'),
    url(r'^stats/u/(?P<id>\d+)/$', 'stats.views.user'),
    url(r'^stats/top10/$', 'stats.views.top10'),
    # Examples:
    # url(r'^$', 'LoUStatsWeb.views.home', name='home'),
    # url(r'^LoUStatsWeb/', include('LoUStatsWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
