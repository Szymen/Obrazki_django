from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    # url(r'^view', 'Obrazki_django.views.home', name='home'),
    url(r'^$' ,       include('img_bro.urls')), # kiedy nie ma nic w pasku poza localhostem

    url(r'admin/', include(admin.site.urls)),
    url(r'', include('img_bro.urls')),
)
