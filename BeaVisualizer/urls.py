from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
                       url(r'(?P<year>\d{4})/(?P<query>\w+)', 'graph', name='graph'),
                       url(r'^$', 'index', name='home'),
                       # url(r'^BeaVisualizer/', include('BeaVisualizer.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
)
