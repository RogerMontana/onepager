from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trex_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', index),

)
