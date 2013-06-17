# -*- coding: utf-8 *-*
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^registro/$', 'usuarios.views.nuevoUserView'), # agregar nuevo usuario
	url(r'^$', 'deudores.views.index'),
	url(r'^instituto/$', 'deudores.views.institutoIndex'),	
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'usuarios/login.html'}),
	url(r'^logout/$', 'usuarios.views.cerrarSesion'),
	url(r'^nuevo/$', 'deudores.views.nuevoDeudor'),
	url(r'^editar/(?P<id_deudor>\d+)$', 'deudores.views.editarDeudor'), 
	url(r'^eliminar/(?P<id_deudor>\d+)$', 'deudores.views.eliminarDeudor'), 
	url(r'^buscador/curp/$', 'deudores.views.buscarDeudorCurp'), 
	url(r'^buscador/generales/$', 'deudores.views.buscarDeudorNombre'),
)


# Esta linea hace que en modo produccion o trabajando con el wsgi funcionen
# los static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()