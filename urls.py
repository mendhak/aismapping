from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'aismap.views.home', name='home'),
    url(r'^raw$', 'aismap.views.rawdata', name='home'),
    url(r'^process', 'aismap.views.storedata', name='home'),
    url(r'^getvisible$', 'aismap.views.getVisibleShips', name='home'),
    url(r'^marinetraffic', 'aismap.views.marinetraffic', name='home'),
    # url(r'^aismapping/', include('aismapping.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
