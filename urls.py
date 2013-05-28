from django.conf.urls.defaults import *
from django.views.static import * 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Example:
                       # (r'^reserva/', include('reserva.foo.urls')),
                       (r'^$', 'main.views.index'),
                       (r'^index/$', 'main.views.index'),
                       (r'^login/$', 'main.views.login_user'),
                       (r'^horario/$', 'main.views.horario'),
                       (r'^nosotros/$', 'main.views.nosotros'),
                       (r'^reservar/$', 'main.views.reservar'),
                       (r'^logout/$', 'main.views.logout_user'),
                       (r'^nueva_noticia/$', 'main.views.nueva_noticia'),
                       (r'^eliminar_noticia/$', 'main.views.eliminar_noticia'),
                       (r'^limpiar_noticias/$', 'main.views.limpiar_noticias'),
                       # Required to make static serving work 
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/favicon.ico'})
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
