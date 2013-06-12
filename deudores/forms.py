# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import Deudor
from django import forms

class DeudorForm(ModelForm):
	class Meta:
		model = Deudor
		exclude = ('fecha_ingreso', 'institucion')

	def clean_nombre(self):
	    return self.cleaned_data['nombre'].upper()

	def clean_apepat(self):
		return self.cleaned_data['apepat'].upper()

	def clean_apemat(self):
	    return self.cleaned_data['apemat'].upper()

        def clean_CURP(self):
            return self.cleaned_data['CURP'].upper()

class BuscarCurpForm(forms.Form):
	CURP = forms.CharField(max_length=18, label=_(u"CURP"))

	def clean_CURP(self):
		return self.cleaned_data['CURP'].upper()


class BuscarNombreForm(ModelForm):
	class Meta:
		model = Deudor
		exclude = ('fecha_ingreso', 'institucion', 'CURP', 'descripcion')

	def clean_nombre(self):
	    return self.cleaned_data['nombre'].upper()

	def clean_apepat(self):
		return self.cleaned_data['apepat'].upper()

	def clean_apemat(self):
	    return self.cleaned_data['apemat'].upper()