# -*- coding: utf-8 *-*
from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from empresa.forms import DeudorForm



def  index(request):
	return render_to_response('index/index.html',  context_instance=RequestContext(request))

@login_required(login_url='/login')
def nuevoDeudor(request):
    if request.method=='POST':
    	formulario = DeudorForm(request.POST)
    	if formulario.is_valid():
    		aux = formulario.save()
    		return HttpResponseRedirect('/instituto')
    else:
    	formulario = DeudorForm()
    return render_to_response('empresas/nueva_empresa.html', {'formulario':formulario}, context_instance=RequestContext(request))





# encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.admin.views.decorators import staff_member_required
from empresa.forms import EmpresaForm, UserEmpresaForm
from empresa.models import UserEmpresa


# Se genera el formulario para agregar una nueva empresa,
# una vez que esta empresa se creo se manda al registro para generar su login.
@staff_member_required
def nueva_empresa(request):
    if request.method=='POST':
    	formulario = EmpresaForm(request.POST)
    	if formulario.is_valid():
    		aux = formulario.save()
    		return HttpResponseRedirect('/empresa/registro/%s' % aux.id)
    else:
    	formulario = EmpresaForm()
    return render_to_response('empresas/nueva_empresa.html', {'formulario':formulario}, context_instance=RequestContext(request))