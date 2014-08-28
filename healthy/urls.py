from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'healthy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.indexVista'),
    url(r'^login/$', 'autenticacion.views.loginView'),
    url(r'^datosjson/$', 'main.views.ver_calendario'),
    url(r'^verfecha/$', 'main.views.ver_fecha'),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
