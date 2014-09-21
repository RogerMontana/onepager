from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import urls as main_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trex_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^superuser/', include(admin.site.urls)),
    url(r'^', include(main_urls))
)
