# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import Deudor
from django import forms

class DeudorForm(ModelForm):
	class Meta:
		model = Deudor
		exclude = ('fecha_ingreso', 'institucion')