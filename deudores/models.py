# -*- coding: utf-8 *-*
from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class Deudor (models.Model):
	nombre = models.CharField(max_length=45, verbose_name=_(u'Nombre'))
	apepat = models.CharField(max_length=45, verbose_name=_(u'Apellido paterno'))
	apemat = models.CharField(max_length=45, verbose_name=_(u'Apellido materno'))
	fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name=_('Fecha de nacimiento'))
	descripcion = models.TextField(verbose_name=_('Descripcion'))
	institucion = models.ForeignKey(User)