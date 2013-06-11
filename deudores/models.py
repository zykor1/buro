# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

choices_estado = (
	('1', 'Debe'),
	('2', 'No debe'))

class Deudor (models.Model):
	nombre = models.CharField(max_length=45, verbose_name=_(u'Nombre'))
	apepat = models.CharField(max_length=45, verbose_name=_(u'Apellido paterno'))
	apemat = models.CharField(max_length=45, verbose_name=_(u'Apellido materno'))
	fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name=_('Fecha de nacimiento'))
	descripcion = models.TextField(verbose_name=_('Descripcion'))
	institucion = models.ForeignKey(User)
	fecha_ingreso = models.DateField(auto_now_add=True, verbose_name=_('Fecha de ingreso'))
	estado = models.CharField(max_length=1, blank=True, verbose_name=_(u'Estado'))
	tipo = models.CharField(max_length=12, blank=True, verbose_name=_(u'Alumno o profesor') )
	CURP = models.CharField(max_length=12, blank=True, verbose_name=_(u'CURP') )

	def __unicode__(self):
		return '%s' %(self.nombre)